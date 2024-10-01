from flask import Flask
from models.models import db
from flask_marshmallow import Marshmallow
import secrets
from routes.song_routes import register_song_routes
from routes.playlist_routes import register_playlist_routes
from routes.player_routes import register_player_routes



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+mysqlconnector://root:*********@localhost/playlist_api"
)
db.init_app(app)
ma = Marshmallow(app)

register_song_routes(app)
register_playlist_routes(app)
register_player_routes(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.secret_key = secrets.token_bytes()
    app.run(debug=True)
