from wtforms import StringField, SubmitField, Form

from wtforms.validators import DataRequired


class UrlForm(Form):
    url = StringField('url', validators=[DataRequired()])
    submit = SubmitField('Convert')


class SongForm(Form):
    title = StringField('title', validators=[DataRequired()])
    artist = StringField('artist')
    album = StringField('album')
    submit = SubmitField('download')