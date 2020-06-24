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
device_name = creds.DEVICE_NAME

def get_device(device_name):
    device_list = sp.devices()['devices']
    device = next(dev for dev in device_list if dev["name"] == device_name)
    return device

def vol_up():
    dev = get_device(device_name)
    vol = dev["volume_percent"]
    if vol < 100:
        vol += 5
    elif vol >= 100:
        vol = 100
    sp.volume(vol, device_id=dev["id"])
    print(f"Volume: {vol}")
    return

def vol_down():
    dev = get_device(device_name)
    vol = dev["volume_percent"]
    if vol > 0:
        vol -= 5
    elif vol <= 0:
        vol = 0
    sp.volume(vol, device_id=dev["id"])
    print(f"Volume: {vol}")
    return

def play_pause():
    dev = get_device(device_name)
    try:
        sp.start_playback(device_id=dev["id"])
        print("Play")
    except:
        sp.pause_playback(device_id=dev["id"])
        print("Pause")
    return

def next_track():
    dev = get_device(device_name)
    try:
        sp.next_track(device_id=dev["id"])
    except:
        print("Can't go next track")
    return

def prev_track():
    dev = get_device(device_name)
    try:
        sp.previous_track(device_id=dev["id"])
    except:
        print("Can't go prev track")
    return

# Setting up key combinations
current = set()
VOL_U = {keyboard.Key.cmd, keyboard.Key.f8}
VOL_D = {keyboard.Key.cmd, keyboard.Key.f7}
PREV = {keyboard.Key.cmd, keyboard.Key.f9}
PLAY_PAUSE = {keyboard.Key.cmd, keyboard.Key.f10}
NEXT = {keyboard.Key.cmd, keyboard.Key.f11}

def on_press(key):
    if key in VOL_D or VOL_U or PREV or PLAY_PAUSE or NEXT:
        current.add(key)
        if all(k in current for k in VOL_D):
            try:
                vol_down()
            except:
                print("Vol down action failed")
        elif all(k in current for k in VOL_U):
            try:
                vol_up()
            except:
                print("Vol up action failed")
        elif all(k in current for k in PLAY_PAUSE):
            play_pause()
        elif all(k in current for k in NEXT):
            next_track()
        elif all(k in current for k in PREV):
            prev_track()

def on_release(key):
    try:
        current.clear()
    except KeyError:
        pass

current.clear()
print("Listening")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()