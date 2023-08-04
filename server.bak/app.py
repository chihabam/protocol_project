import socket
from flask import Flask
from flask_restful import Api
from Device import Device 
from Room import Room 
from Home import Home
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8040))
print("Socket bound to " + sock.getsockname()[0])
sock.listen()
print("Server listening...")

def client_handler(c_socket):
    while True:
        data = c_socket.recv(1024).decode().strip()
        if not data:
            break
        response= "Received data:"
        print(response, data)

        c_socket.send(response.encode())
    c_socket.close()



def run():
    sequence_num=0

    
    while True:
        connectionSocket, addr = sock.accept()
        print("CONNECTED SOURCE: " + str(addr))
        # connectionSocket.close()
        r = Home(True,True, 65)
        # r.leave_routine()
        c_socket,c_addr= sock.accept()
        client_handler_thread = threading.Thread(
        target=client_handler, args=(c_socket,)
        )
        client_handler_thread.start()

run()       
