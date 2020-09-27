from socket import *
from tkinter import *
from main import jewelryCombineMain, jewelryCombineMain2, jewelryCombineMain3

window = Tk()

window.title('편하게 살자')
window.geometry("200x72+100+100")
window.resizable(True,True)

b1 = Button(window, text = '보석 낱개 조합', command=jewelryCombineMain2)
b2 = Button(window, text = '퍼보 만들어 보석 조합', command=jewelryCombineMain)
b3 = Button(window, text = '통합 조합', command=jewelryCombineMain3)
b1.pack(fill=X)
b2.pack(fill=X)
b3.pack(fill=X)
window.mainloop()


