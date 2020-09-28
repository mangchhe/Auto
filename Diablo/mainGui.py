from socket import *
from tkinter import *
from tkinter import messagebox
from main import jewelryCombineMain, jewelryCombineMain2, jewelryCombineMain3
import threading
import time
from pynput.keyboard import Listener, Key
 
def handlePress( key ):
    pass
 
def handleRelease( key ):
    if key == Key.f2:
        jewelryCombineMain3()
 
def execute():
    with Listener(on_press=handlePress, on_release=handleRelease) as listener:
        listener.join()

def doSomething():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

window = Tk()

thread = threading.Thread(target=execute)
thread.daemon = True
thread.start()

window.title('편하게 살자')
window.geometry("200x72+100+100")
window.resizable(True,True)
window.protocol('WM_DELETE_WINDOW', doSomething)

b1 = Button(window, text = '보석 낱개 조합', command=jewelryCombineMain2)
b2 = Button(window, text = '퍼보 만들어 보석 조합', command=jewelryCombineMain)
b3 = Button(window, text = '통합 조합', command=jewelryCombineMain3)
b1.pack(fill=X)
b2.pack(fill=X)
b3.pack(fill=X)

window.mainloop()


