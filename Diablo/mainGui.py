from socket import *
from tkinter import *
from main import jewelryCombineMain

clientSock = socket(AF_INET, SOCK_STREAM)
try:
    clientSock.connect(('192.168.0.4', 8888))
    data = clientSock.recv(1024)
    if data.decode() == 'ver1.0':
        window = Tk()

        window.title('편하게 살자')
        window.geometry("200x24+100+100")
        window.resizable(True,True)

        b1 = Button(window, text = '보석 조합', command=jewelryCombineMain)
        b1.pack(fill=BOTH)
        window.mainloop()
    else:
        print('버전이 다릅니다.')
except:
    print('서버가 닫혔습니다.')

