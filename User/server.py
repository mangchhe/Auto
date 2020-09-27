from socket import *
from datetime import datetime

count = 0

now = datetime.now()

with open('log.txt', 'a') as file:
    file.write("\n시작 : {}년 {}월 {}일 {}시 {}분\n".format(now.year, now.month, now.day, now.hour, now.minute))

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8888))
serverSock.listen()

while True:
    clientSock, addr = serverSock.accept()
    clientSock.send('ver1.0'.encode())
    count +=1
    print('방문 아이피 :', addr)
    print('방문 횟수 :', count)
    with open('log.txt', 'a') as file:
        file.write(str(addr) + ' 에서 접속이 확인되었습니다.\n')
        file.write('방문 횟수 : ' + str(count) +'\n')
