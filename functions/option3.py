"""
This file's purpose is to hold the option3 function(s) // Procedure(s)
"""
try:
    # All imports required for procedures // functions to work correctly.
    import spotipy
    from huepy import green, info
    from time import sleep
    # Required for obtaining token for procedure user_top_tracks.
    from .authentication import user_auth
    from .spotiterm_func import clear
except ImportError as err:
    print(f"Failed to import modules for option3.py: {err}")

"""
Option 3 Lookup a user's top tracks. Short and long term.
Returns:
    None.
Args:
    username_token: Received from user_auth() in authentication.py
Exceptions:
    spotipy.client.SpotifyException
    TypeError
"""


def user_top_tracks(username_token):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            # clear() to remove authentication text.
            clear()
            sp = spotipy.Spotify(auth=token)
            print(green("Short Term Tracks"))
            resp = sp.current_user_top_tracks(
                time_range="short_term", limit=10)
            for i, item in enumerate(resp["items"], 1):
                # Prints item number. Track name, artist name.
                print(
                    green(f" {i} {item['name']} -- {item['artists'][0]['name']}"))
            print(green("Long Term Tracks"))
            resp = sp.current_user_top_tracks(time_range="long_term", limit=10)
            for i, item in enumerate(resp["items"], 1):
                print(
                    green(f" {i} {item['name']} -- {item['artists'][0]['name']}"))
            # Sleep for user to observe output.
            sleep(15)
        else:
            print(green(f"Can't get token for {username}"))
            sleep(2)
    except spotipy.client.SpotifyException as err:
        print(green(f"User Top Track Lookup Failed: {err}"))
        sleep(2)
    except TypeError as err:
        print(green(f"Failed to get redirect URL from browser: {err}"))
        sleep(2)
