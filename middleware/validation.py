from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()

class SongSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    artist = fields.String(required=True)
    release_date = fields.Date(required=True)

    class Meta:
        fields = ("id", "name", "artist", "release_date")

class PlaylistSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    song_ids = fields.List(fields.Integer(), required=True)

    class Meta:
        fields = ("id", "name", "song_ids")
