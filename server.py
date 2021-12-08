#!/usr/bin/python3
import socket
import threading

#python 3.1 script for IM server

#TCP Server Class
class TCP_server :
    #constructor to generate and bind socket
    def __init__(self):
        print("Constructor called")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.sock.bind(('localhost', 5000))
        self.sock.listen(5)
        print("Constructor finished")
    def get_msg(ip):
        print("waiting on message")
        while True:
            print("still here")
            try:
                msg = ip.recv(1024).decode()
                print(str(msg))
                ip.sendall(bytes(msg))
            except Exception as e:
                break
        #print(str(ip) + " disconnected")
    #server sits in idle waiting for a connection
    def go(self):
        while True:
            print("Server go called")
            #accept connection
            client_name,addr = self.sock.accept()
            conn = threading.Thread(target = self.get_msg(), args = (client_name,addr))
            conn.start()
            #receive message
            #msg = client_name.recv(1024).decode()
            #send confirmation of msg rec
            #client_name.send(("Message received").encode())
            #print(str(addr) + " " + str(msg))

def main():
    #instatiate and go
    server = TCP_server()
    print("Server Initialized")
    server_const = threading.Thread(target=server.go())
    print("Threads Initialized")
    server_const.start()
    print("Server Started")
if __name__ == "__main__":
    main()