# SpotiTerm
![SpotiTerm](spotiterm.png)

A Terminal Interface to perform actions with Spotify's Web API.

## Disclaimer
This is my first project I have ever uploaded to Github, so please keep this in mind if I'm a little slow. Still adjusting and learning the flow. Thanks, Dextroz.

## Dependencies
SpotiTerm is written in Python 3 so it is **REQUIRED**.

SpotiTerm requires the following dependencies:
  1. * [Spotipy](https://github.com/plamere/spotipy) - A light weight Python library for the Spotify Web API.
  2. * [Hue](https://github.com/UltimateHackers/hue) - Provides a minimal and powerful interface to print colored text and labels in the terminal.

## Download Options -- Installing
Currently you can only clone or download the project ZIP file.

Extract and Navigate to the zipfile directory and run SpotiTerm by executing the main entry point file (SpotiTerm.py):
  ```
  python3 SpotiTerm.py
  ```

## Prerequisites
To operate SpotiTerm you must:
  
  1. Have a **Spotify** Account.

  1. Go to Spotify's developer website and [create an application](https://beta.developer.spotify.com/dashboard/login). 
  
  2. Go to your applications settings and add you're preferred redirect URI (I chose "http://localhost:8888").
  
  3. Navigate to you're apps dashboard and copy the Client ID and Client Secret.
  
  4. Place **Client ID** and **Client Secret** in the respective variables found in [config.py](config.py):
      ```
      CLIENT_ID = "Insert Client ID Here"
      CLIENT_S = "Insert Client Secret Here"
      REDIRECT_URI = "Insert Redirect URI Here."
      ```
## Authors -- Contributors

* **Daniel Brennand** - *Author* - [Dextroz](https://github.com/Dextroz)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.

## Acknowledgments

* Spotipy created by Paul Lamere (plamere) and respective contributors.
* Hue created by Somdev Sangwan (UltimateHackers) and respective contributors.
