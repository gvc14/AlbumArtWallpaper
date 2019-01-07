# AlbumArtWallpaper
Set album art of currently playing song on spotify as your Desktop Wallpaper.

# Usage:

First open a developer aaccount on Spotify. Create a new project, then get client-id and secret. In settings menu of your project add a redirect-uri (http://localhost/callback can also be used). 
        
Then `python3 AlbumArtWallpaper.py`

# Requirement:

Needs [Spotipy](https://github.com/plamere/spotipy)

# Limitations:
Works for a linux system running gnome 3+, however, the code can be changed accordingly. 

By modifying ` os.system("gsettings set org.gnome.desktop.background picture-uri " + link)` in the script.
