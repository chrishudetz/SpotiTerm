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
    from .spotiterm_func import clear
except ImportError as err:
    print(f"Failed to import modules for option4.py: {err}")

"""
Option 4 Get user's top artists; short and long term.
Args:
    username_token: Received from user_auth() in authentication.py
Exceptions:
    spotipy.client.SpotifyException
    TypeError
"""


def user_top_artist(username_token):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            # clear() to remove authentication text.
            clear()
            sp = spotipy.Spotify(auth=token)
            print(green("Short Term Artists"))
            resp = sp.current_user_top_artists(
                time_range="short_term", limit=10)
            for i, item in enumerate(resp["items"], 1):
                # Prints user's top short term artists.
                print(green(f" {i} {item['name']}"))
            print(green("Long Term Artists"))
            resp = sp.current_user_top_artists(
                time_range="long_term", limit=10)
            for i, item in enumerate(resp["items"], 1):
                # Prints user's top long term artists.
                print(green(f" {i} {item['name']}"))
            sleep(15)
        else:
            print(green(f"Can't get token for {username}"))
            sleep(2)
    except spotipy.client.SpotifyException as err:
        print(green(f"User Top Artist Lookup Failed: {err}"))
        sleep(2)
    except TypeError as err:
        print(green(f"Failed to get redirect URL from browser: {err}"))
        sleep(2)
