"""
This file's purpose is to hold the option5 function(s) // Procedure(s)
"""
try:
    # All imports required for procedures // functions to work correctly.
    import spotipy
    from huepy import green, info
    from time import sleep
    # Required for obtaining token for procedure playlist_contents.
    from .authentication import user_auth
except ImportError:
    print("Failed to import modules for option5.py")

"""
Option 5 lists artist name and track name.
Args:
    resp = tracks passed in from playlist_contents() when procedure is invoked.
"""


def list_tracks(resp):
    # For number, item in resp.
    for i, item in enumerate(resp["items"]):
        track = item["track"]
        # Print artist -- track name.
        print(green(" ""{} -- {}".format(
            track["artists"][0]["name"], track["name"])))


"""
Option 5 Iterates through User owned playlists printing the total number of
tracks and [Artist] -- [trackname]
Args:
    username_token: Received from user_auth() in authentication.py
Exceptions:
    spotipy.client.SpotifyException
"""


def playlist_contents(username_token):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            sp = spotipy.Spotify(auth=token)
            # Holds all user playlists.
            playlists = sp.user_playlists(username)
            # For each playlist in playlists variable.
            for playlist in playlists["items"]:
                # Check is owner and ID is equal to username provided.
                if playlist["owner"]["id"] == (username):
                    print()
                    print(green(" ""{}".format(playlist["name"])))
                    # Slows down output. Gives user time to read.
                    sleep(1)
                    print(green(" ""Total Tracks: {}".format(
                        playlist["tracks"]["total"])))
                    # Slows down output. Gives user time to read.
                    sleep(1)
                    resp = sp.user_playlist(
                        username, playlist["id"], fields="tracks,next")
                    tracks = resp["tracks"]
                    list_tracks(tracks)
                    # While still more tracks. Continue listing tracks.
                    while tracks["next"]:
                        tracks = sp.next(tracks)
                        list_tracks(tracks)
            print()
            print(green(" ""User's Playlists displayed above."))
            # Sleep to allow user to observe output.
            sleep(25)
        else:
            print(green("Can't get token for {}".format(username)))
            sleep(2)
    except spotipy.client.SpotifyException:
        print(green("Playlist Lookup Failed."))
        sleep(2)
    except TypeError:
        print(green("Failed to get redirect URL from browser."))
        sleep(2)