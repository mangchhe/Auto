from tkinter import *
from main import jewelryCombineMain

window = Tk()

window.title('편하게 살자')
window.geometry("200x24+100+100")
window.resizable(True,True)

b1 = Button(window, text = '보석 조합', command=jewelryCombineMain)

b1.pack(fill=BOTH)

window.mainloop()