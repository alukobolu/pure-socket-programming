import socket
from threading import *

s =socket.socket()
print("Sockets created")

s.bind(('localhost',9099))

s.listen()
print("waiting for connection")

clients = []
names = []

class notification:
    def talk(self,message):
        for c in clients:
            c.send(message)

    def manager(self,c):
        while True:
            try:
                message = c.recv(1024)
                self.talk(message)
            except:
                id = clients.index(c)
                clients.remove(c)
                c.close()
                Cname = names[id]
                names.remove(Cname)
                self.talk(bytes('{} left the chat'.format(Cname),"utf-8"))
                break

class recieve(notification):
    def run(self):
        while True:
            c,addr= s.accept()
            print("connected with",addr)

            c.send(bytes("NAMEFUNC","utf-8"))
            name = c.recv(1024).decode()
            names.append(name)
            clients.append(c)
            
            print('Client name is {}'.format(name))
            self.talk(bytes("{} joined the chat".format(name),"utf-8"))
            c.send(bytes("Connected to the chat","utf-8"))

            thred = Thread(target=self.manager, args=(c,))
            thred.start()
print('server is listening...')           
main = recieve()
main.run()