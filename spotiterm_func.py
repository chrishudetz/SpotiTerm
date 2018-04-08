"""
This file currently holds all functions and procedures for executing each
menu option. This file's functions/procedures are ordered by menu options.

Future Development is for seperation of concerns. I am currently working on this
but having issues with imports :-(
"""
try:
    # Import auth and user_auth functions for use in SpotiTerm.py
    from authentication import *
    # Import platform for use in clear() and browser_open().
    import platform
    # Import subprocess for use in clear() and browser_open().
    import subprocess
except ImportError:
    print("Imports failed.")

"""
The main_options procedure prints the logo and all menu options.
"""


def menu_options():
    logo()
    # green() is from huepy. Helps stick to colour scheme.
    print(green(" ""1. Track Search"))
    print(green(" ""2. Artist Top 10"))
    print(green(" ""3. Get User's Top Tracks"))
    print(green(" ""4. Get User's Top Artists"))
    print(green(" ""5. Show User's Playlists Tracks"))
    print(green(" ""6. Add -- Delete Track(s) From Playlist"))
    print(green(" ""7. Exit SpotiTerm"))


"""
Logo procedure.
"""


def logo():
    print(green("""
       ___           _   _ _____
      / __|_ __  ___| |_(_)_   _|__ _ _ _ __
      \__ \ '_ \/ _ \  _| | | |/ -_) '_| '  |
      |___/ .__/\___/\__|_| |_|\___|_| |_|_|_|
          |_|
    Created By: Daniel Brennand a.k.a: Dextroz
         """))


"""
Terminal Clear.
Exceptions:
    subprocess.CalledProcessError
"""


def clear():
    try:
        # execute "cls" if os is windows else execute "clear".
        subprocess.call(["cls" if platform.system() == "Windows" else "clear"])
    except subprocess.CalledProcessError:
        print(green("Terminal clear failed."))
        sleep(2)


"""
Option 1 function. Searches track specified by user.
Returns:
    url
Args:
    sp: auth() from authentication.py
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
                clear()
    except subprocess.CalledProcessError:
        print(green("Failed. Check your system has Chrome installed."))
        sleep(2)


"""
Option 2. Lookup an Artists top 10 tracks. Specified by user.
Args:
    sp: auth() from authentication.py
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
            print(green("Token could not be recieved for {}".format(username)))
            sleep(2)
    except spotipy.client.SpotifyException:
        print(green("User Top Artist Lookup Failed."))
        sleep(2)
    except TypeError:
        print(green("Failed to get redirect URL from browser."))
        sleep(2)


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


"""
Option 6. This function is called within playlist(). Asks if the user wants to
add one or more tracks. Asks for track URI input(s) and returns variable for
usage in playlist()
Returns:
    2 x track_ids
"""


def add_del_track():
    try:
        track_numbers = input(
            info(green("One or more tracks: One or More: ")))
        if (track_numbers) == ("More"):
            # Input tracks seperated by ","
            track_ids = input(
                info(green("Track Ids seperated by , : "))).split(",")
            # Return track_ids for use in playlist()
            return track_ids
        elif (track_numbers) == ("One"):
            # Single track ID select. Input track ID.
            track_ids = input(info(green("Input track ID: "))).split()
            # Return track_ids for use in playlist()
            return track_ids
        else:
            print(green("Input a valid option: "))
            add_del_track()
    except:
        print(green("An error occured in add_del_track()"))
        sleep(2)
        clear()
        print(green("""
                    add_del_track function failed.
                    Ensure you added , when adding more than one track."""))


"""
Option 6 playlist(). Given a playlist ID. Add or delete track(s) from a given
playlist.
Args:
    username_token: Received from user_auth() in authentication.py
Exceptions:
    spotipy.client.SpotifyException
    TypeError
"""


def playlist(username_token):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            sp = spotipy.Spotify(auth=token)
            playlist_id = input(info(green("Please enter the Playlist ID: ")))
            add_delete = input(info(green("Add or Delete Tracks: ")))
            if (add_delete) == ("Add"):
                # Invokes add_del_track and stores return inside track_ids.
                track_ids = add_del_track()
                # Holds resp from function add tracks. Passes in track_ids
                # returned from add_del_track()
                resp = sp.user_playlist_add_tracks(
                    username, playlist_id, track_ids)
                # If successfull; print tracks added.
                print(green(" ""Track(s) Added."))
            elif (add_delete) == ("Delete"):
                # Holds resp from function add tracks. Passes in track_ids
                # returned from add_del_track()
                track_ids = add_del_track()
                resp1 = sp.user_playlist_remove_all_occurrences_of_tracks(
                    username, playlist_id, track_ids)
                # Prints if successfull.
                print(green(" ""Track(s) Removed."))
            else:
                # If neither Add or Delete specified. Exit to main menu.
                print(green("Neither Add or Delete; Exiting to main menu."))
        else:
            print(green("Can't get token for {}".format(username)))
            sleep(2)
            clear()
        # Sleep to observe short output. Then exits to main menu.
        sleep(2)
        clear()
    except spotipy.client.SpotifyException:
        print(green("Failed to Add // Delete Track(s)"))
        sleep(2)
    except TypeError:
        print(green("Failed to get redirect URL from browser."))
        sleep(2)
