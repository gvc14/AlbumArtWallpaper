import wget
import spotipy
import spotipy.util as util
import time
import os
import config

scope = config.scope
username = config.username
client_id = config.client_id
client_secret = config.client_secret
redirect_uri = config.redirect_uri

def tokenGen():
    token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret,
                                       redirect_uri=redirect_uri)
    sp = spotipy.Spotify(auth=token)
    return sp

def run_mac():
    sp = tokenGen()
    sp.trace = True
    while True:
        user = sp.currently_playing()
        temp = user
        try:
            time.sleep(5)
            user = sp.currently_playing()
            if temp["item"]["album"]["id"] == user["item"]["album"]["id"]:
                continue
            else:
                old_filename = temp['item']['album']['images'][0]['url'].split("/")[-1]
                print(old_filename)
                old_absolute_filename = os.path.join(
                    os.path.abspath(os.getcwd()), old_filename)
                os.system(f"rm {old_absolute_filename}")
                link = user['item']['album']['images'][0]['url']
                local_filename = wget.download(link)
                full_local_filename = os.path.abspath(local_filename)
                print(full_local_filename)
                os.system(
                    f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"{full_local_filename}\"'")
                time.sleep(5)
        except spotipy.client.SpotifyException:
            sp = tokenGen()
            continue

def run_linux():
    sp = tokenGen()
    sp.trace = True
    while True:
        user = sp.currently_playing()
        temp = user
        try:
            time.sleep(5)
            user = sp.currently_playing()
            if temp["item"]["album"]["id"] == user["item"]["album"]["id"]:
                continue
            else:
                link = user['item']['album']['images'][0]['url']
                os.system("gsettings set org.gnome.desktop.background picture-uri " + link)
                time.sleep(5)
        except spotipy.client.SpotifyException:
            sp = tokenGen()
            continue

def run_windows():
    print("Windows is not currently supported")

def main():
    platform = os.sys.platform
    if platform == "darwin":
        run_mac()
    elif platform in ("linux1", "linux2"):
        run_linux()
    elif platform == "win32":
        run_windows()

if __name__ == '__main__':
    main()



