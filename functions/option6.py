"""
This file's purpose is to hold the option6 function(s) // Procedure(s)
"""
try:
    # All imports required for procedures // functions to work correctly.
    import spotipy
    from huepy import green, info
    from time import sleep
    from .authentication import user_auth
    from .spotiterm_func import clear
except ImportError as err:
    print(f"Failed to import modules for option6.py: {err}")

"""
Option 6. This function is called within playlist(). Asks if the user wants to
add one or more tracks. Asks for track URI input(s) and returns variable for
usage in playlist()
Returns:
    track_ids
"""


def add_del_track():
    try:
        print(info(green("Input one or more track(s): seperated by , if multiple")))
        # Input tracks, seperated by "," if multiple.
        track_ids = input(info(green("Tracks: "))).split(",")
        return track_ids
    # Exception here is unlikely however, basic handle has been done.
    except:
        print(green("""
                    add_del_track function failed.
                    Ensure you added , when adding more than one track."""))
        sleep(2)


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
            # clear() to remove authentication text.
            clear()
            sp = spotipy.Spotify(auth=token)
            playlist_id = input(info(green("Please enter the Playlist ID: ")))
            add_delete = input(info(green("Add or Delete Tracks: ")))
            if (add_delete) == ("Add"):
                # Invokes add_del_track and stores return inside track_ids.
                track_ids = add_del_track()
                # Holds resp from function add tracks. Passes in track_ids
                # returned from add_del_track()
                sp.user_playlist_add_tracks(
                    username, playlist_id, track_ids)
                # If successfull; print tracks added.
                print(green(" ""Track(s) Added."))
            elif (add_delete) == ("Delete"):
                # Holds resp from function add tracks. Passes in track_ids
                # returned from add_del_track()
                track_ids = add_del_track()
                sp.user_playlist_remove_all_occurrences_of_tracks(
                    username, playlist_id, track_ids)
                # Prints if successfull.
                print(green(" ""Track(s) Removed."))
            else:
                # If neither Add or Delete specified. Exit to main menu.
                print(green("Neither Add or Delete; Exiting to main menu."))
        else:
            print(green(f"Can't get token for {username}"))
            sleep(2)
        # Sleep to observe short output. Then exits to main menu.
        sleep(2)
    except spotipy.client.SpotifyException as err:
        print(green(f"Failed to Add // Delete Track(s): {err}"))
        sleep(2)
    except TypeError as err:
        print(green(f"""
                    Track Inputs Failed. Failed to get redirect URL from browser.
                    {err}
                    """))
        sleep(2)
