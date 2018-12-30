import sys
import spotipy
import spotipy.util as util
import os
import time

scope = 'user-library-read'
interval = 5  #Wallpaper change frequency

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Username: " % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
for item in results['items']:   			
    link = item['track']['album']['images'][0]['url']	
    os.system("gsettings set org.gnome.desktop.background picture-uri " + link)
    time.sleep(interval)

