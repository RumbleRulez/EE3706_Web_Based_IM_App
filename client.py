#!/usr/bin/python3
import socket
import threading


#Python 3.1 Client for TCP

#TCP Client Class
class TCP_conn_client: # (threading.Thread):
    #calls constructor to generate socket and connect
    def __init__(self):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #self.sock.connect((socket.gethostname(),5000))
            self.sock.connect(('localhost',5000))
    #send message function
    def send_msg(self, msg):
        self.sock.send((msg).encode())
    #receive message function
    def recieve_msg(self):
        print(self.sock.recv(1024).decode())
    #Print a menu WIP
    def print_menu():
        print("Hello, welcome to an IM service.")

def main():    
    #instantiate a client object
    client = TCP_conn_client()
    #loop
    while True:
        client.send_msg(input("Message: "))
        client.recieve_msg()

        #send_thread = threading.Thread(client.send_msg(input("Message: ")))        
        #send_thread.start()

        #rec_thread = threading.Thread(client.recieve_msg())
        #rec_thread.start()


if __name__ == "__main__":
    main()