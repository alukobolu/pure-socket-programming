import socket

s =socket.socket()
print("socket created ")

#binding socket to port
s.bind(('localhost',10999))

s.listen(3)
print("Waiting for client to connect")

while True:
    c,addr= s.accept()
    
    name = c.recv(1024).decode()

    print("connected with",addr,name)

    c.send(bytes("this is the begining of greatness","utf-8"))

    c.close()