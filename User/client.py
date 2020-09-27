from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
try:
    clientSock.connect(('127.0.0.1', 8888))
    data = clientSock.recv(1024)
    if data.decode() == 'ver1.0':
        print('버전이 일치합니다.')
    else:
        print('버전이 다릅니다.')
except:
    print('서버가 닫혔습니다.')