from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

playlist_songs = db.Table('playlist_songs',
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'), primary_key=True),
    db.Column('song_id', db.Integer, db.ForeignKey('songs.id'), primary_key=True)
)

class Song(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255))
    release_date = db.Column(db.DateTime)

class Playlist(db.Model):
    __tablename__ = "playlists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    song_ids = db.relationship('Song', secondary=playlist_songs, backref='playlists', lazy='dynamic')

    def add_song(self, song):
        if song not in self.song_ids:
            self.song_ids.append(song)
            db.session.commit()

    def remove_song(self, song):
        if song in self.song_ids:
            self.song_ids.remove(song)
            db.session.commit()
