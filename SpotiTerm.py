"""
Main Entry point for SpotiTerm. Contains spotiterm main menu.
"""
try:
    # Import all functions for usage in SpotiTerm.py (main entry.)
    from huepy import green, info
    from time import sleep
    from functions.authentication import user_auth, auth
    from functions.spotiterm_func import menu_options, logo, clear
    from functions.option1 import track_search, browser_open
    from functions.option2 import artist_top_10
    from functions.option3 import user_top_tracks
    from functions.option4 import user_top_artist
    from functions.option5 import playlist_contents
    from functions.option6 import playlist
    from functions.option7 import get_devices, player_controls
except ImportError as err:
    print(f"Imports Failed: {err}")
    
"""
The main menu procedure for SpotiTerm
"""


def spotiterm():
    # While loop to always go back to menu after action performed.
    while (True):
        # Clear terminal.
        clear()
        # Prints menu options (See spotiterm_func.py)
        menu_options()
        user_input = input(
            info(green("Select a menu option: ")))
        if (user_input) == ("1"):
            clear()
            # Executes track_search(), passing in auth() return (sp object) into
            # it. Then browser_open() executes.
            browser_open(track_search(auth()))
        elif (user_input) == ("2"):
            clear()
            # Executes artist_top_10(), passing in auth() return (sp object).
            artist_top_10(auth())
        elif (user_input) == ("3"):
            clear()
            # Executes user_top_tracks(), user_auth() passed in to get username
            # and token for use. Scope passed in for user_auth().
            user_top_tracks(user_auth("user-top-read"))
        elif (user_input) == ("4"):
            clear()
            # Executes user_top_artist(), user_auth() passed in to get username
            # and token for use. Scope passed in for user_auth().
            user_top_artist(user_auth("user-top-read"))
        elif (user_input) == ("5"):
            clear()
            # Executes playlist_contents(), user_auth() passed in to get username
            # and token for use. Scope passed in for user_auth().
            playlist_contents(user_auth("playlist-read-private"))
        elif (user_input) == ("6"):
            clear()
            # Asks user if a public or private playlist is for tracks to be
            # removed or deleted from.
            public_private = input(
                info(green("Public or Private Playlist: ")))
            if (public_private) == ("Public"):
                public_scope = "playlist-modify-public"
                # Executes playlist(), user_auth() passed in to get username
                # and token for use. Scope passed in for user_auth().
                playlist(user_auth(public_scope))
            elif (public_private) == ("Private"):
                private_scope = "playlist-modify-private"
                # Executes playlist(), user_auth() passed in to get username
                # and token for use. Scope passed in for user_auth().
                playlist(user_auth(private_scope))
            else:
                print(green("Input a valid menu option."))
                sleep(2)
        elif (user_input) == ("7"):
            clear()
            player_controls(get_devices(user_auth("user-read-playback-state")))
        elif (user_input) == ("8"):
            clear()
            exit()
        else:
            # Catch invalid menu option input.
            print(green("Input a valid menu option."))
            sleep(2)


spotiterm()
