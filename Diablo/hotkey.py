from pynput.keyboard import Listener, Key
import time
import threading
from jewelry import Jewelry
from room import Room

class Hotkey:

    def __init__(self, jewelry, room):
        self.jewelry = jewelry
        self.room = room

    def handlePress(self, key):
        pass
    
    def handleRelease(self, key):
        keyClick = str(key)
        if key == Key.f9:
            self.jewelry.jewelryCombineMain2()
        if key == Key.f10:
            self.room.TogetherMain()
        if key == Key.f11:
            self.room.EachMain()
    
    def execute(self):
        with Listener(on_press=self.handlePress, on_release=self.handleRelease) as listener:
            listener.join()

    def hotkeyMain(self):
        thread = threading.Thread(target=self.execute)
        thread.daemon = True
        thread.start()