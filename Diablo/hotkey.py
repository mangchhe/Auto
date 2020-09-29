from pynput.keyboard import Listener, Key
import time
import threading

from jewelry import jewelryCombineMain, jewelryCombineMain2, jewelryCombineMain3

def handlePress( key ):
    pass
 
def handleRelease( key ):
    if key == Key.f2:
        jewelryCombineMain()
    if key == Key.f3:
        jewelryCombineMain2()
    if key == Key.f4:
        jewelryCombineMain3()
 
def execute():
    with Listener(on_press=handlePress, on_release=handleRelease) as listener:
        listener.join()

def hotkeyMain():
    thread = threading.Thread(target=execute)
    thread.daemon = True
    thread.start()