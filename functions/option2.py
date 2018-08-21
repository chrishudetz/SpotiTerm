"""
This file's purpose is to hold the option2 function(s) // Procedure(s)
"""
try:
    # All imports required for procedures // functions to work correctly.
    import spotipy
    from huepy import green, info
    from time import sleep
    from .authentication import auth
    # For exception in procedure.
    import spotipy.oauth2
except ImportError as err:
    print(f"Failed to import modules for option2.py: {err}")

"""
Option 2. Lookup an Artists top 10 tracks. Specified by user.
Args:
    sp: auth() from authentication.py; Returns sp object.
Exceptions:
    spotipy.client.SpotifyException
    spotipy.oauth2.SpotifyOauthError
"""


def artist_top_10(sp):
    try:
        artist_name = input(info(green("What is the artist name: ")))
        # resp for searching artist name. Get top artist tracks.
        resp = sp.search(q=artist_name, limit=10)
        # int: 1 is passed to start from 1 instead of 0.
        for item, track in enumerate(resp["tracks"]["items"], 1):
            print(green(f" {item} {track['name']}"))
        # Sleep to observe above print.
        sleep(8)
    except spotipy.client.SpotifyException as err:
        print(green(f"Top 10 track lookup failed: {err}"))
        sleep(2)
    except spotipy.oauth2.SpotifyOauthError as err:
        print(green(f"Bad request. Check Client ID and Client S: {err}"))
        sleep(2)
