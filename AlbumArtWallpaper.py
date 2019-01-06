import spotipy
import spotipy.util as util
import time
import os
interval = 1
scope = 'user-read-currently-playing'
username = 'Your Username'
def tokenGen():
        token = util.prompt_for_user_token(username,scope,client_id = 'Your_client_id',client_secret='Your_client_secret',
                                           redirect_uri='http://localhost:8888/callback/')
        sp = spotipy.Spotify(auth=token)
        return sp
sp = tokenGen()
sp.trace = True
print(sp.currently_playing())
while True:
    user = sp.currently_playing()
    temp = user
    try:
     time.sleep(5)
     user = sp.currently_playing()
     if temp == user:
         continue
     else:
         link = user['item']['album']['images'][0]['url']
         os.system("gsettings set org.gnome.desktop.background picture-uri " + link)
         time.sleep(5)
    except spotipy.client.SpotifyException:
     sp = tokenGen()
     continue
