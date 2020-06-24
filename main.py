# https://github.com/moses-palmer/pynput/issues/20 
from pynput import keyboard
import spotipy
import spotipy.util as util
import creds

scope = 'user-modify-playback-state user-read-playback-state'
token = util.prompt_for_user_token(creds.USERNAME,
                           scope,
                           client_id=creds.CLIENT_ID, 
                           client_secret=creds.CLIENT_SECRET,
                           redirect_uri=creds.REDIRECT_URI)

sp = spotipy.client.Spotify(auth=token)
# device_name = input("Device name: ")
device_name = "LAPTOP-T34QML4F"
def get_device(device_name):
    device_list = sp.devices()['devices']
    device = next(dev for dev in device_list if dev["name"] == device_name)
    print(device["volume_percent"])
    return device

def vol_up():
    dev = get_device(device_name)
    vol = dev["volume_percent"]
    if vol < 100:
        vol += 5
    elif vol >= 100:
        vol = 100
    sp.volume(vol, device_id=dev["id"])
    return

def vol_down():
    dev = get_device(device_name)
    vol = dev["volume_percent"]
    if vol >= 100:
        vol -= 5
    elif vol <= 0:
        vol = 0
    sp.volume(vol, device_id=dev["id"])
    return

# def prev_track():

# def play_pause():

# def next_track():

#Play pause key
VOL_D   = {keyboard.Key.cmd, keyboard.Key.f7}
VOL_U   = {keyboard.Key.cmd, keyboard.Key.f8}
PREV    = {keyboard.Key.cmd, keyboard.Key.f9}
PLAY    = {keyboard.Key.cmd, keyboard.Key.f10}
NEXT    = {keyboard.Key.cmd, keyboard.Key.f11}

# Active set
current = set()

def on_press(key):
    if key in VOL_D or VOL_U or PREV or PLAY or NEXT:
        current.add(key)
        if all(k in current for k in VOL_D):
            vol_down()
        elif all(k in current for k in VOL_U):
            vol_up()
        elif all(k in current for k in PREV):
            print("Prev")
        elif all(k in current for k in PLAY):
            print("Play")
        elif all(k in current for k in NEXT):
            print("Next")

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()