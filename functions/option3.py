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
except ImportError:
    print("Failed to import modules for option3.py")

"""
Option 3 Lookup a user's top tracks. Short and long term.
Returns:
    None.
Args:
    username_token: Received from user_auth() in authentication.py
Exceptions:
    spotipy.client.SpotifyException
"""


def user_top_tracks(username_token):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            sp = spotipy.Spotify(auth=token)
            short_term = "short_term"
            long_term = "long_term"
            print(green("Short Term Tracks"))
            resp = sp.current_user_top_tracks(time_range=short_term, limit=11)
            for i, item in enumerate(resp["items"]):
                # Prints item number. Track name, artist name.
                print(green(" ""{} {} {} {}".format(
                    i, item["name"], "--", item["artists"][0]["name"])))
            print(green("Long Term Tracks"))
            resp1 = sp.current_user_top_tracks(time_range=long_term, limit=11)
            for i, item in enumerate(resp1["items"]):
                # Prints item number. Track name, artist name.
                print(green(" ""{} {} {} {}".format(
                    i, item["name"], "--", item["artists"][0]["name"])))
            # Sleep for user to observe output.
            sleep(15)
        else:
            print(green("Token could not be recieved for {}".format(username)))
            sleep(2)
    except spotipy.client.SpotifyException:
        print(green("User Top Track Lookup Failed."))
        sleep(2)
    except TypeError:
        print(green("Failed to get redirect URL from browser."))
        sleep(2)
