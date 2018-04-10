"""
This file's purpose is to hold the option4 function(s) // Procedure(s)
"""
try:
    # All imports required for procedures // functions to work correctly.
    import spotipy
    from huepy import green, info
    from time import sleep
    # Required for obtaining token for procedure user_top_artist.
    from .authentication import user_auth
except ImportError:
    print("Failed to import modules for option4.py")

"""
Option 4 Get user's top artists; short and long term.
Args:
    username_token: Received from user_auth() in authentication.py
Exceptions:
    spotipy.client.SpotifyException
"""


def user_top_artist(username_token):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            sp = spotipy.Spotify(auth=token)
            short_term = "short_term"
            long_term = "long_term"
            print(green("Short Term Artists"))
            resp = sp.current_user_top_artists(time_range=short_term, limit=11)
            for i, item in enumerate(resp["items"]):
                # Prints user's top short term artists.
                print(green(" ""{} {}".format(i, item["name"])))
            print(green("Long Term Artists"))
            resp1 = sp.current_user_top_artists(time_range=long_term, limit=11)
            for i, item in enumerate(resp1["items"]):
                # Prints user's top long term artists.
                print(green(" ""{} {}".format(i, item["name"])))
            sleep(15)
        else:
            print(green("Can't get token for {}".format(username)))
            sleep(2)
    except spotipy.client.SpotifyException:
        print(green("User Top Artist Lookup Failed."))
        sleep(2)
    except TypeError:
        print(green("Failed to get redirect URL from browser."))
        sleep(2)
