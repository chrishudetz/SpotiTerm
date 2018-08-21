"""
This file holds the two authentication functions. user_auth() for user
authentication required functions and auth() for functions which don't require
user authentication.
"""
try:
    from huepy import green, info
    # Client ID, Client Secret, Redirect uri (for user_auth())
    from .config import CLIENT_ID, CLIENT_S, REDIRECT_URI
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    import spotipy.util as util
    from time import sleep
except ImportError as err:
    print(f"Imports failed for authentication.py: {err}")

"""
User authentication function. Asks for Spotify Username and scope is passed in for use
for specific options.
Args:
    scope = passed in as str when called at SpotiTerm.py
Returns:
    username, token
Exceptions:
    spotipy.oauth2.SpotifyOauthError
"""


def user_auth(scope):
    try:
        username = input(info(green("Spotify Username: ")))
        # Token variable. scope passed in when called in SpotiTerm.py
        token = util.prompt_for_user_token(
            username, scope, client_id=CLIENT_ID, client_secret=CLIENT_S, redirect_uri=REDIRECT_URI, cache_path=f".cache-{username}")
        return username, token
    except spotipy.oauth2.SpotifyOauthError:
        print("User Authentication Failed.")
        sleep(2)


"""
Authentication function for non user required data (ie: Track search e.t.c.).
Returns:
    sp object.
Exceptions:
    spotipy.oauth2.SpotifyOauthError
"""


def auth():
    try:
        # authorisation. Gets token for functions. CLIENT_ID and CLIENT_SECRET passed in.
        client_credentials = SpotifyClientCredentials(
            client_id=CLIENT_ID, client_secret=CLIENT_S)
        # sp currently for global use.
        sp = spotipy.Spotify(client_credentials_manager=client_credentials)
        # Return sp object. For use in non user required calls to API.
        return sp
    except spotipy.oauth2.SpotifyOauthError:
        print("Authentication Failed! Check connection or CLIENT_ID or CLIENT_SECRET keys.")
        sleep(2)
