"""
This file holds menu_options, logo and clear functions // procedures.
Seperation of concerns has been addressed.
"""
try:
    # Import platform for use in clear()
    import platform
    # Import subprocess for use in clear()
    import subprocess
    # Import sleep from time for use in clear()
    from time import sleep
    # Import green from huepy to keep with colour scheme.
    from huepy import green
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
