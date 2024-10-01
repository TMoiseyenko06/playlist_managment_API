
# Playlist API Project

A basic playlist API project made for basic use only.


## Authors

- [@Tmoiseyenko06](https://www.github.com/Tmoiseyenko06)


## Installation

Clone the github repository

```bash
  git clone https://github.com/TMoiseyenko06/playlist_managment_API.git
```
    
## Run Locally

Go to the project directory

```
  cd my-project
```

Make sure to set up your database 

```
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+mysqlconnector://root:*********@localhost/playlist_api"
)
```
Set up the VENV
 
Run the flask app

```
flask run 
```
## Routes

- Create playlist
- Create Song
- Add song to playlist
- Delete playlist
- Load playlist
- Sort playlist
- Play playlist
- Play next song
- Play previous song

