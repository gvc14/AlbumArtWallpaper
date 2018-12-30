# AlbumartWallpaper
Simple python script to change your desktop background periodically by album arts of saved songs from your Spotify library.
Usage:
First open a developer aaccount on Spotify. Create a new project, then get client-id and secret. In settings menu of your project add a redirect-uri (http://localhost/callback can also be used). 

first setup environment variables before running the script:

`export SPOTIPY_CLIENT_ID='your-spotify-client-id'     #project-id`

`export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'  #secret-key to the project`

`export SPOTIPY_REDIRECT_URI='your-app-redirect-url'   #redirect-url that you have assigned`
            
Then `python3 AlbumArtWallpaper.py 'your username on spotify'`

You can change the frequency by changing value of `interval` in the script.
