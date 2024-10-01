from flask import request, jsonify
from marshmallow import ValidationError
from models.models import db, Song
from middleware.validation import SongSchema, PlaylistSchema

song_schema = SongSchema()


def register_song_routes(app):
    @app.route('/songs', methods=['POST'])
    def create_song():
        try:
            song_data = song_schema.load(request.json)
        except ValidationError as e:
            return jsonify({"Error": f'{e}'}), 400
        
        new_song = Song(
            name=song_data["name"],
            artist=song_data["artist"],
            release_date=song_data["release_date"]
        )
        db.session.add(new_song)
        db.session.commit()
        return jsonify({"response": "Song Added"}), 200

    @app.route('/songs/<int:id>', methods=["DELETE"])
    def delete_song(id):
        song = Song.query.get_or_404(id)
        db.session.delete(song)
        db.session.commit()
        return jsonify({"message": "song deleted"}), 200

    @app.route('/songs/<int:id>', methods=['PUT'])
    def update_song(id):
        song = Song.query.get_or_404(id)
        try:
            song_data = song_schema.load(request.json)
        except ValidationError as e:
            return jsonify({"Error": f'{e}'}), 400
        
        song.name = song_data["name"]
        song.artist = song_data["artist"]
        song.release_date = song_data["release_date"]

        db.session.commit()
        return jsonify({"message": "Song updated"}), 200
