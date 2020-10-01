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
    if key == Key.f2:
        jewelry.jewelryCombineMain2()
    if key == Key.f3:
        jewelry.jewelryCombineMain()
    if key == Key.f4:
        jewelry.jewelryCombineMain3()
    if key == Key.f5:
        room.TogtherMain()
    if key == Key.f6:
        room.EachMain()
 
def execute():
    with Listener(on_press=handlePress, on_release=handleRelease) as listener:
        listener.join()

def hotkeyMain():
    thread = threading.Thread(target=execute)
    thread.daemon = True
    thread.start()