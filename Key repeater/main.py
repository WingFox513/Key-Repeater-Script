from pynput.keyboard import Controller, Listener, Key  
import time

controller = Controller()
running = False
press_interval = 0.01

def on_press(key):
    global running
    try:
        if key.char == 'r':     #Change to some key within quotes to make that key the repeater key
            running = True
            print("Starting the Restart Repeater...(Press 'f' to stop)")
        elif key.char == 'f':
            running = False
            print("The Restart Repeater has been stopped.")
    except AttributeError:
        pass

def on_release(key):
    global running 
    try:
        if key == Key.esc:
            return False
    except AttributeError:
        pass

listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

try:
    while True:
        if running:
            controller.press('r')
            controller.release('r')
            time.sleep(press_interval)
        else:
            time.sleep(0.01)
except KeyboardInterrupt:
    print("Program has been terminated")
    listener.stop()
