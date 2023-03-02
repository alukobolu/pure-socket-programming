import socket
from threading import *

c =socket.socket()

c.connect(('localhost',9099))

name=input("enter your name :")



def recieve():
    while True:
        try:
            data = c.recv(1024).decode()
            if data =="NAMEFUNC":
                c.send(bytes(name,'utf-8'))
            else:
                print(data)
        except:
            print("An error occurred ")
            c.close()
            break

def send():
    while True:
        message = input("message :")
        c.send(bytes("{}:{}".format(name,message),"utf-8"))

recv_thred = Thread(target = recieve)
recv_thred.start()

send_thred = Thread(target = send)
send_thred.start()