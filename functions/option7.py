"""
This file's purpose is to hold the option7 function(s) // Procedure(s)
"""
try:
    # All imports required for procedures // functions to work correctly.
    import spotipy
    from huepy import green, info
    from time import sleep
    from .authentication import user_auth
    from .spotiterm_func import clear
    # Used in play_pause()
    from .option6 import add_del_track
except ImportError:
    print("Failed to import modules for option7.py")

"""
This procedure is the menu for the player controls option. Executed from
Spotiterm.py
Args:
    device_info: Passed from get_devices() Executed at Spotiterm.py
Exceptions:
    UnboundLocalError: Occurs when selecting device.
    TypeError: Occurs if get_devices fails.
"""


def player_controls(device_info):
    try:
        # Unload device variables for usage.
        name_choice, id_choice = device_info
        if name_choice:
            # Stay in menu once option has finished.
            while (True):
                clear()
                # Show device selected from get_devices()
                print(
                    green(" ""Device: {} -- ID: {} selected.".format(name_choice, id_choice)))
                print()
                print(green(" ""1. Currently Playing Info"))
                print(green(" ""2. Play -- Pause -- Resume"))
                print(green(" ""3. Next -- Previous"))
                print(green(" ""4. Shuffle"))
                print(green(" ""5. Seek"))
                print(green(" ""6. Set Volume"))
                print(green(" ""7. Back to Main Menu"))
                user_input = input(info(green("Select Player Option: ")))
                if (user_input) == ("1"):
                    # Clear executed to remove authentication text.
                    clear()
                    current_play(user_auth("user-read-currently-playing"))
                elif (user_input) == ("2"):
                    clear()
                    play_pause(user_auth("user-modify-playback-state"),
                               name_choice, id_choice)
                elif (user_input) == ("3"):
                    clear()
                    next_previous(
                        user_auth("user-modify-playback-state"), name_choice, id_choice)
                elif (user_input) == ("4"):
                    clear()
                    # Ask for state. Enable or Disable shuffling.
                    state = input(info(green("Enable or Disable: ")))
                    if (state) == ("Enable"):
                        clear()
                        # Set to True to enable.
                        shuffle(
                            user_auth("user-modify-playback-state"), True, id_choice)
                    elif (state) == ("Disable"):
                        clear()
                        # Set to False to disable.
                        shuffle(
                            user_auth("user-modify-playback-state"), False, id_choice)
                    else:
                        print(green("Input a valid option."))
                        sleep(2)
                elif (user_input) == ("5"):
                    clear()
                    seek_track(user_auth("user-modify-playback-state"),
                               name_choice, id_choice)
                elif (user_input) == ("6"):
                    clear()
                    set_volume(user_auth("user-modify-playback-state"),
                               name_choice, id_choice)
                elif (user_input) == ("7"):
                    # break while loop to roll back to main menu (spotiterm())
                    break
                else:
                    print(green("Input a valid menu option."))
                    sleep(2)
        else:
            print("Couldn't get device name or ID.")
            sleep(2)
    except UnboundLocalError:
        print(green("Failed to get device information."))
        sleep(2)
    except TypeError:
        print(green("Failed to get device information."))
        sleep(2)


"""
Get devices currently avaliable for playback on user's account.
Args:
    username_token: Passed from user_auth(): authentication.py
Exceptions:
    spotipy.client.SpotifyException: Occurs if sp.devices() fails.
    UnboundLocalError: Occurs if out of range device is selected.
Returns:
    name_choice, id_choice
"""


def get_devices(username_token):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            # clear() to remove authentication text.
            clear()
            sp = spotipy.Spotify(auth=token)
            resp = sp.devices()
            # List objects.
            device_id_list = []
            device_name_list = []
            # For device names and ids in resp, append each to corresponding
            # list.
            for item, devices in enumerate(resp["devices"]):
                device_name_list.append(devices["name"])
                device_id_list.append(devices["id"])
                device_name = devices["name"]
                device_id = devices["id"]
                print(green(
                    " ""Device: {} -- Name: {} -- Device ID: {}".format(item, device_name, device_id)))
            user_input = input(info(green("Select Device Number: ")))
            # Start from 0 due to python indexing starting at 0.
            # Support currently for only 4 devices. This is due to my own lack of knowledge.
            # Which ever device selected: Select data from corresponding lists.
            if (user_input) == ("0"):
                id_choice = device_id_list[0]
                name_choice = device_name_list[0]
            elif (user_input) == ("1"):
                id_choice = device_id_list[1]
                name_choice = device_name_list[1]
            elif (user_input) == ("2"):
                id_choice = device_id_list[2]
                name_choice = device_name_list[2]
            elif (user_input) == ("4"):
                id_choice = device_id_list[3]
                name_choice = device_name_list[3]
            return name_choice, id_choice
        else:
            print(green("Can't get token for {}".format(username)))
            sleep(2)
    except spotipy.client.SpotifyException:
        print(green("Failed to get devices."))
        sleep(2)
    except UnboundLocalError:
        print(green("Please select a valid device."))
        sleep(2)


"""
See information about the current playing track
Args:
    username_token: Passed from user_auth(): authentication.py
Exceptions:
    spotipy.client.SpotifyException: Occurs if sp.currently_playing() fails.
"""


def current_play(username_token):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            # clear() to remove authentication text.
            clear()
            sp = spotipy.Spotify(auth=token)
            resp = sp.currently_playing(market="GB")
            is_playing = resp["is_playing"]
            progress_ms = resp["progress_ms"]
            track_name = resp["item"]["name"]
            album_name = resp["item"]["album"]["name"]
            artist_name = resp["item"]["album"]["artists"][0]["name"]
            print(info(green("Track: {} -- Album: {} -- Artist: {} -- Playing: {} -- Progress: {}".format(
                track_name, album_name, artist_name, is_playing, progress_ms))))
            sleep(10)
        else:
            print(green("Can't get token for {}".format(username)))
    except spotipy.client.SpotifyException:
        print(green("Failed to get current playing track."))
        sleep(2)


"""
Play, Pause or Resume playback.
Args:
    username_token: Passed from user_auth(): authentication.py
    name_choice: Passed in at execution from player_controls()
    id_choice: Passed in at execution from player_controls()
Exceptions:
    spotipy.client.SpotifyException: Occurs if player is already playing,
    playback is already paused.
No exceptions for username_token unload as exception occurs in player_controls()
"""


def play_pause(username_token, name_choice, id_choice):
    # Unpack returns from user_auth(): authentication.py
    username, token = username_token
    if token:
        # clear() to remove authentication text.
        clear()
        sp = spotipy.Spotify(auth=token)
        user_input = input(info(green("Play, Pause or Resume: ")))
        if (user_input) == ("Play"):
            # Ask if playing an album, artist or playlist or track(s)
            user_input = input(
                info(green("Album, Artist, Playlist or Track(s): ")))
            if ((user_input) == ("Album")) or ((user_input) == ("Artist")) or ((user_input) == ("Playlist")):
                try:
                    # Enter context URI
                    user_input = input(info(green("Enter URI: ")))
                    resp = sp.start_playback(
                        device_id=id_choice, context_uri=user_input)
                    print(green(" ""Playback Started on {}".format(name_choice)))
                    sleep(2)
                except spotipy.client.SpotifyException:
                    # Except if playback already occuring.
                    print(green(" ""Already playing. Please pause."))
                    sleep(2)
            elif ((user_input) == ("Track")) or ((user_input) == ("Tracks")):
                try:
                    # Input track(s) add_del_track() called for re-use.
                    # from option6.py
                    resp = sp.start_playback(
                        device_id=id_choice, uris=add_del_track())
                    print(green(" ""Playback Started on {}".format(name_choice)))
                    sleep(2)
                except spotipy.client.SpotifyException:
                    print(green(" ""Already playing. Please pause."))
                    sleep(2)
            else:
                # Else statement if neither album, artist, playlist or track(s).
                # selected.
                print(green("Input a valid menu option."))
                sleep(2)
        elif (user_input) == ("Pause"):
            try:
                # Pause playback device.
                resp = sp.pause_playback(device_id=id_choice)
                print(green(" ""Paused on {}".format(name_choice)))
                sleep(2)
            except spotipy.client.SpotifyException:
                print(green("Playback already paused."))
                sleep(2)
        elif (user_input) == ("Resume"):
            try:
                # Resume playback device.
                resp = sp.start_playback(device_id=id_choice)
                print(green(" ""Resuming playback on {}".format(name_choice)))
                sleep(2)
            except spotipy.client.SpotifyException:
                print(green(" ""Already Playing."))
                sleep(2)
        else:
            # else statement if neither Play, pause or resume is selected.
            print(green("Input a valid menu option."))
            sleep(2)
    else:
        print(green("Can't get token for {}".format(username)))
        sleep(2)


"""
Skip to the next or previous track on the selected player device.
Args:
    username_token: Passed from user_auth(): authentication.py
    state: Passed in at execution from player_controls()
    id_choice: Passed in at execution from player_controls()
Exceptions:
    2 x spotipy.client.SpotifyException: Occurs if fails to skip.
"""


def next_previous(username_token, name_choice, id_choice):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            # clear() to remove authentication text.
            clear()
            sp = spotipy.Spotify(auth=token)
            user_input = input(info(green("Next or Previous?: ")))
            if (user_input) == ("Next"):
                # Skip track.
                resp = sp.next_track(device_id=id_choice)
                print(green(" ""Track skipped on {}".format(name_choice)))
                sleep(2)
            elif (user_input) == ("Previous"):
                try:
                    # Previous track.
                    resp = sp.previous_track(device_id=id_choice)
                    print(green(" ""Previous track on {}".format(name_choice)))
                except spotipy.client.SpotifyException:
                    print(green("No previous track avaliable."))
                    sleep(2)
            else:
                print(green("Input a valid menu option."))
                sleep(2)
        else:
            print(green("Can't get token for {}".format(username)))
    except spotipy.client.SpotifyException:
        print(green("Failed to skip -- go to previous track."))


"""
Enable or disable shuffle for player.
Args:
    username_token: Passed from user_auth(): authentication.py
    state: Passed in at execution from player_controls()
    id_choice: Passed in at execution from player_controls()
Exceptions:
    spotipy.client.SpotifyException: Occurs if sp.shuffle() fails.
"""


def shuffle(username_token, state, id_choice):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            # clear() to remove authentication text.
            clear()
            sp = spotipy.Spotify(auth=token)
            # State passed in from player_controls() Can be True or False.
            resp = sp.shuffle(state, device_id=id_choice)
            print(green(" ""Complete."))
            sleep(2)
        else:
            print(green("Can't get token for {}".format(username)))
            sleep(2)
    except spotipy.client.SpotifyException:
        print(green("Failed to shuffle."))
        sleep(2)


"""
Seek to a specified ms time of a track.
Args:
    username_token: Passed from user_auth(): authentication.py
    name_choice: Passed in at execution from player_controls()
    id_choice: Passed in at execution from player_controls()
Exceptions:
    spotipy.client.SpotifyException: Occurs if fails to seek track.
    ValueError: Occurs if a non integer is inputted.
"""


def seek_track(username_token, name_choice, id_choice):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            sp = spotipy.Spotify(auth=token)
            # clear() to remove authentication text.
            clear()
            progress_input = input(info(green("Skip to? (ms): ")))
            # Convert input to int.
            progress_int = int(progress_input)
            resp = sp.seek_track(progress_int, device_id=id_choice)
            print(green(" ""Track seeked to {} ms on {}.".format(
                progress_int, name_choice)))
            sleep(2)
        else:
            print(green("Can't get token for {}".format(username)))
    except spotipy.client.SpotifyException:
        print(green("Failed to seek to point on track."))
        sleep(2)
    except ValueError:
        print(green("Input only an integer."))
        sleep(2)


"""
Set the volume for playback device.
Args:
    username_token: Passed from user_auth(): authentication.py
    name_choice: Passed in at execution from player_controls()
    id_choice: Passed in at execution from player_controls()
Exceptions:
    spotipy.client.SpotifyException: Occurs if volume fails to set.
"""


def set_volume(username_token, name_choice, id_choice):
    try:
        # Unpack returns from user_auth(): authentication.py
        username, token = username_token
        if token:
            # clear() to remove authentication text.
            clear()
            sp = spotipy.Spotify(auth=token)
            # Asks for volume input. String due to Hue function usage.
            volume = input(info(green("Volume: ")))
            # String input converted into integer.
            volume_int = int(volume)
            if (volume_int) >= (0) and (volume_int) <= (100):
                resp = sp.volume(volume_int, device_id=id_choice)
                print(green(" ""Volume set to {} for {}".format(
                    volume_int, name_choice)))
                sleep(2)
            else:
                print(green("Volume must be between 0 and 100 or equal to."))
                sleep(2)
        else:
            print(green("Can't get token for {}".format(username)))
            sleep(2)
    except spotipy.client.SpotifyException:
        print(green("Failed to set volume."))
        sleep(2)
    except ValueError:
        print(green("Input only an integer."))
        sleep(2)
