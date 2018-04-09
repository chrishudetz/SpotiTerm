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
    import subprocess
    import platform
    from .spotiterm_func import clear
except ImportError:
    print("Failed to import modules for option1.py")

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
        resp = sp.search(q="track:" + track_name, limit=1,
                         type="track", market="GB")
        for item, track in enumerate(resp["tracks"]["items"]):
            # Gets URL for song searched.
            url_dict = track["external_urls"]
            # Gets URL value from key "spotify" in dict.
            url = url_dict.get("spotify")
            # Prints trackname and its spotify URL.
            print(green(" ""Track: {}, URL: {}".format(track["name"], url)))
            # Returns URL so it can be used in browser_open()
            return url
    except spotipy.client.SpotifyException:
        print(green("Track lookup failed."))
        sleep(2)
    except spotipy.oauth2.SpotifyOauthError:
        print(green("Bad Request. Check Client ID, Client S."))
        sleep(2)


"""
Option 1 browser_open. Opens specified user track in Google Chrome.
Args:
    URL. Passed from track_search()
Exceptions:
    subprocess.CalledProcessError
"""


def browser_open(url):
    try:
        if url:
            user_input = input(
                green("Open track in Google Chrome: Yes or No "))
            if (user_input) == ("Yes"):
                # Holds result for os check.
                user_platform = platform.system()
                # If Darwin (Mac)
                if (user_platform) == ("Darwin"):
                    # Execute command to open Google Chrome with url
                    subprocess.call(
                        ["/usr/bin/open", "-a", "/Applications/Google Chrome.app", url])
                elif (user_platform) == ("Linux"):
                    subprocess.call(["google-chrome", url])
                elif (user_platform) == ("Windows"):
                    subprocess.call(["chrome.exe", url])
            else:
                # If any other input ie No. clear to main menu (spotiterm)
                pass
    except subprocess.CalledProcessError:
        print(green("Failed. Check your system has Chrome installed."))
        sleep(2)
