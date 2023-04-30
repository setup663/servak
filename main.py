from socket import *
from sqlite3 import *


class server:
    def __init__(self, ip, port):
        self.serv = socket(AF_INET, SOCK_STREAM)
        self.serv.bind((ip, port))
        self.serv.listen(2)


    def sender(self, user, text):
        user.send(text.encode('utf-8'))


    def start_server(self):
        while True:
            user, addr = self.serv.accept()
            print('Client connected')
            self.listen(user)


    def listen(self, user):
        self.sender(user, 'connected')
        is_work = True
        while is_work:
            try:
                data = user.recv(1024)
                self.sender(user, 'getted')
            except:
                data = ''
                is_work = False
            if len(data) > 0:
                msg = data.decode('utf-8')
                if msg == 'disconnect':
                    self.sender(user, 'You are disconnect')
                    user.close()
                    is_work = False
                else:
                    print(msg)
            else:
                print('Client disconnect')
                is_work = False




server('192.168.0.83', 7000).start_server()