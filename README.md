# spotiPy-ctrl
Control local instance of spotify using shortcuts

**Why?**

I want to play/pause the music but oftentimes I find chrome interrupting and it randomly plays some random youtube video that I forgot to close or don't want to close

## Usage:
- WinKey + F10 = pause spotify
- WinKey + F09 = prev
- WinKey + F11 = next
- WinKey + F07 = vol decrease
- WinKey + F08 = vol increase

## Credentials
- Edit the ``_creds.py`` and remove underscore

## Setup
1. Setting up spotify app
  - Go to your spotify [Dashboard](https://developer.spotify.com/dashboard/applications)
  - Copy over your client id and client secret
  - Add ``http://localhost:9090`` as *Redirect URI*
  
 2. Install requirements
  - ``pip install -r requirements.txt``
  
 3. Edit keys if you desire
 
 4. Run it and control your spotify via these key combinations

## Citation (??)
>Pynput combo keys method: https://github.com/moses-palmer/pynput/issues/20 
