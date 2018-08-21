"""
This file's purpose is to hold the option1 function(s) // Procedure(s)
"""
try:
    # All imports required for procedures // functions to work correctly.
    import spotipy
    from huepy import green, info
    from time import sleep
    from .authentication import auth
    # For exception in function (track_search)
    import spotipy.oauth2
    import webbrowser
except ImportError as err:
    print(f"Failed to import modules for option1.py: {err}")

"""
Option 1 function. Searches track specified by user.
Returns:
    url
Args:
    sp: auth() from authentication.py; Returns sp object.
Exceptions:
    spotipy.client.SpotifyException
"""


def track_search(sp):
    try:
        # User input for trackname
        track_name = input(info(green("What is the track name?")))
        # Resp holding results from search track.
        resp = sp.search(q=f"track:{track_name}", limit=1,
                         type="track", market="GB")
        for item, track in enumerate(resp["tracks"]["items"]):
            # Gets URL for song searched.
            url = track["external_urls"]["spotify"]
            # Prints trackname and its spotify URL.
            print(green(f" Track: {track['name']}, url: {url}"))
            # Returns URL so it can be used in browser_open()
            return url
    except spotipy.client.SpotifyException:
        print(green("Track lookup failed."))
        sleep(2)
    except spotipy.oauth2.SpotifyOauthError:
        print(green("Bad Request. Check Client ID, Client S."))
        sleep(2)


"""
Option 1 browser_open. Opens specified user track in default system web browser.
Args:
    URL. Passed into this procedure.
Exceptions:
    webbrowser.Error
"""


def browser_open(url):
    try:
        if url:
            user_input = input(
                green("Open track in your browser?: Yes or No "))
            if (user_input) == ("Yes"):
                # Opens URL in default system browser.
                webbrowser.open(url)
            else:
                # If any other input ie No. Exit to main menu (spotiterm)
                pass
    except webbrowser.Error:
        print(green("Failed to open url in your browser."))
        sleep(2)
