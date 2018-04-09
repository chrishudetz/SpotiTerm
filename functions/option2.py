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
except ImportError:
    print("Failed to import modules for option2.py")

"""
Option 2. Lookup an Artists top 10 tracks. Specified by user.
Args:
    sp: auth() from authentication.py; Returns sp object.
Exceptions:
    spotipy.client.SpotifyException
"""


def artist_top_10(sp):
    try:
        artist_name = input(info(green("What is the artist name: ")))
        # resp for searching artist name. Get top artist tracks.
        resp = sp.search(q=artist_name, limit=11)
        for item, track in enumerate(resp["tracks"]["items"]):
            print(green(" ""{} {}").format(item, track["name"]))
        # Sleep to observe above print.
        sleep(8)
    except spotipy.client.SpotifyException:
        print(green("Top 10 track lookup failed."))
        sleep(2)
    except spotipy.oauth2.SpotifyOauthError:
        print(green("Bad request. Check Client ID and Client S."))
        sleep(2)
