from flask import request, jsonify
from marshmallow import ValidationError
from middleware.validation import PlaylistSchema,SongSchema
from models.models import db, Playlist, Song

playlist_schema = PlaylistSchema()
song_schema = SongSchema()


def register_playlist_routes(app):
    @app.route('/playlists',methods=['POST'])
    def create_playlist():
        try:
            playlist_data = playlist_schema.load(request.json)
        except ValidationError as e:
            return jsonify({"Error":f'{e}'})
        
        new_playlist = Playlist(
            name=playlist_data['name'],
        )
        song_ids = playlist_data['song_ids']
        if song_ids:
            songs = Song.query.filter(Song.id.in_(song_ids)).all()
            new_playlist.song_ids.extend(songs)
        db.session.add(new_playlist)
        db.session.commit()

        return jsonify({"message":"playlist created"})
    
    @app.route('/playlists/<int:id>',methods=['DELETE'])
    def delete_playlist(id):
        playlist = Playlist.query.first_or_404(id)
        print(playlist)
        db.session.delete(playlist)
        db.session.commit()

        return jsonify({"message":"playlist deleted"})
    
    @app.route('/playlists/<int:id>',methods=['PUT'])
    def update_playlist(id):
        playlist = Playlist.query.filter_by(id=id).first_or_404()
        try:
            playlist_data = playlist_schema.load(request.json)
        except ValidationError as e:
            return jsonify({"Error":f"{e}"})

        playlist.name = playlist_data.get("name", playlist.name)  
    
        song_ids = playlist_data.get("song_ids", [])
        if song_ids is not None:  
            playlist.song_ids = song_ids 
    
        db.session.commit()

        return jsonify({"message":"playlist updated"})
    

    @app.route('/playlists/<int:id>',methods=['GET'])
    def get_playlist(id):
        playlist = Playlist.query.first_or_404(id)
        return jsonify(playlist_schema.dump(playlist))

    @app.route('/playlists/songs/<int:playlist_id>/<int:song_id>',methods=['POST','DELETE'])
    def edit_songs(playlist_id,song_id):
        playlist = Playlist.query.first_or_404(playlist_id)
        if request.method == 'POST':
            song = Song.query.get(song_id)
            playlist.add_song(song)
            return jsonify({"message":"song added"})
        elif request.method == 'DELETE':
            song = Song.query.get(song_id)
            playlist.remove_song(song)
            return jsonify({"message":"song deleted"})
        




