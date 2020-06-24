from pynput import keyboard

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
            print("Volume down")
        elif all(k in current for k in VOL_U):
            print("Volume up")
        elif all(k in current for k in PREV):
            print("Prev")
        elif all(k in current for k in PLAY):
            print("Play")
        elif all(k in current for k in NEXT):
            print("Next")
    if key == keyboard.Key.esc:
        listener.stop()

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()