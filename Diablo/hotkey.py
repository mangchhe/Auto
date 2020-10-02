from pynput.keyboard import Listener, Key
import time
import threading
from jewelry import Jewelry
from room import Room

jewelry = Jewelry()
room = Room()

def handlePress( key ):
    pass
 
def handleRelease( key ):
    keyClick = str(key)
    if key == Key.f9:
        jewelry.jewelryCombineMain3()
    if key == Key.f10:
        room.TogetherMain()
    if key == Key.f11:
        room.EachMain()
 
def execute():
    with Listener(on_press=handlePress, on_release=handleRelease) as listener:
        listener.join()

def hotkeyMain():
    thread = threading.Thread(target=execute)
    thread.daemon = True
    thread.start()