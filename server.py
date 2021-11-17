#!/usr/bin/python3
import socket
import threading

#python 3.1 script for IM server

#TCP Server Class
class TCP_server :
    #constructor to generate and bind socket
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        #self.sock.bind((socket.gethostname(), 5000))
        self.sock.bind(('localhost', 5000))
        self.sock.listen(5)
    
    #server sits in idle waiting for a connection
    def go(self):
        #accept connection
        client_name,addr = self.sock.accept()
        print("Connection: " + str(addr))
        #receive message
        msg = client_name.recv(1024).decode()
        #send confirmation of msg rec
        client_name.send(("received").encode())
        print(str(msg))

def main():
    while True:
        #instatiate and go
        server = TCP_server()
        server.go()

if __name__ == "__main__":
    main()