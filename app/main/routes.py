import os

from flask import render_template, current_app, flash, send_file, redirect, request
from mp3_tagger import MP3File

from app import db
from app.main import bp
from app.main.forms import SongForm, UrlForm
from app.main.youtube_dl import YoutubeDL
from app.models import Song


@bp.route('/convert_next/<int:song_id>')
def convert_next(song_id):
    song = Song.query.get_or_404(song_id)
    location = os.path.join(current_app.config['MP3_FOLDER'], song.media_id)
    os.remove(location)
    db.session.delete(song)
    db.session.commit()
    return redirect('/')


@bp.route('/download/<int:song_id>')
def download(song_id):
    try:
        song = Song.query.get_or_404(song_id)
        location = os.path.join(current_app.config['MP3_FOLDER'], song.media_id)
        mp3_file = MP3File(location)
        mp3_file.album = song.album
        mp3_file.artist = song.artist
        mp3_file.save()
    except Exception as e:
        flash('Uups, something goes wrong... SORRY!', 'error')
    return send_file(location, attachment_filename=f'{song.title}.mp3', as_attachment=True)


@bp.route('/convert/<int:song_id>', methods=['GET', 'POST'])
def convert(song_id):
    form = SongForm(request.form)
    if request.method == 'POST':
        if form.validate():
            song = Song.query.get_or_404(song_id)
            song.title = form.title.data
            song.album = form.album.data
            song.artist = form.artist.data
            db.session.add(song)
            db.session.commit()
            return redirect(f'/download/{song_id}')
        else:
            flash('Field "Test" is required.', 'error')
    song = Song.query.get_or_404(song_id)
    return render_template('convert.html', song=song, form=form)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = UrlForm(request.form)
    if request.method == 'POST':
        if form.validate():
            try:
                url = form.url.data
                ydl = YoutubeDL(os.path.join(current_app.config['MP3_FOLDER']))
                song = ydl.convert_url_to_mp3(url)
                db.session.add(song)
                db.session.commit()
                return redirect(f'/convert/{song.id}')
            except Exception as e:
                flash(f'Uups, something goes wrong... SORRY!', 'error')
        else:
            flash('Field "YouTube-URL" is required.', 'error')
    return render_template('index.html', form=form)
