from app import db


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media_id = db.Column(db.String(500), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=True)
    album = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Song {self.id}: {self.title}>'
