from flask import request, jsonify
from marshmallow import ValidationError
from middleware.validation import PlaylistSchema, SongSchema
from models.models import db, Playlist, Song, playlist_songs
from services.to_linked_list import LinkedList

playlist_schema = PlaylistSchema()
song_schema = SongSchema()
current_playlist = LinkedList()

def register_player_routes(app):
    @app.route('/player/playlist/<int:id>',methods=['GET'])
    def load_playlist(id):
        playlist =  Playlist.query.get_or_404(id)
        songs = playlist.song_ids.all()
        for song in songs:
            current_playlist.add_song(song_schema.dump(song))
        return jsonify({"message":"playlist loaded"})
    
    @app.route('/player/play',methods=['GET'])
    def play_song():
        return jsonify(current_playlist.play())
    
    @app.route('/player/play/next',methods=['GET'])
    def play_next():
        return jsonify(current_playlist.play_next())
    
    @app.route('/player/play/prev',methods=['GET'])
    def play_prev():
        return jsonify(current_playlist.play_prev())
    
    @app.route('/playlist/sort/<int:id>/<string:criteria>',methods=['GET'])
    def sort_songs(criteria,id):
        
        playlist =  Playlist.query.get_or_404(id)
        songs = playlist.song_ids.all()
        list_songs = [song_schema.dump(song) for song in songs]
        print(list_songs)
        try:
            list_songs.sort(key=lambda x: x[criteria])
        except:
            return jsonify({"Error":"Error sorting playlist"})
        current_playlist.clear()
        for song in list_songs:
            current_playlist.add_song(song)
        current_playlist.play()
        return jsonify({"message":"playlist sorted and loaded"})

        
        
        


        

    
        
            
        
        


        