"""
Main Entry point for SpotiTerm. Contains spotiterm main menu.
"""
try:
    # Import all functions for usage from spotiterm_func
    from spotiterm_func import *
except ImportError:
    print("Functions file failed to import.")

"""
The main menu procedure for SpotiTerm
"""


def spotiterm():
    # Clears terminal before menu prints.
    clear()
    # While loop to always go back to menu when action performed.
    while (True):
        # Prints menu options.
        menu_options()
        user_input = input(
            info(green("Select a menu option: ")))
        if (user_input) == ("1"):
            clear()
            # Executes track_search(), passing in auth() return (sp object) into
            # it. Then browser_open() executes.
            browser_open(track_search(auth()))
            # Clear terminal when finished.
            clear()
        elif (user_input) == ("2"):
            clear()
            # Executes artist_top_10(), passing in auth() return (sp object) into
            # it.
            artist_top_10(auth())
            clear()
        elif (user_input) == ("3"):
            clear()
            # Executes user_top_tracks(), user_auth() passed in to get username
            # and token for user_top_tracks(). Scope is also passsed in for
            # user_auth() to use.
            user_top_tracks(user_auth("user-top-read"))
            clear()
        elif (user_input) == ("4"):
            clear()
            user_top_artist(user_auth("user-top-read"))
            clear()
        elif (user_input) == ("5"):
            clear()
            playlist_contents(user_auth("playlist-read-private"))
            clear()
        elif (user_input) == ("6"):
            clear()
            # Asks user if a public or private playlist is for tracks to be
            # remmoved or deleted.
            public_private = input(
                info(green("Public or Private Playlist: ")))
            if (public_private) == ("Public"):
                public_scope = "playlist-modify-public"
                # Scope is passed in as variable for user_auth()
                playlist(user_auth(public_scope))
                clear()
            elif (public_private) == ("Private"):
                private_scope = "playlist-modify-private"
                # Scope is passed in as variable for user_auth()
                playlist(user_auth(private_scope))
                clear()
            else:
                clear()
        elif (user_input) == ("7"):
            clear()
            exit()
        else:
            # Catch invalid menu option input.
            print(green("Input a valid menu option."))
            sleep(2)
            clear()


spotiterm()
