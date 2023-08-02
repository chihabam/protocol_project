import socket
from flask import Flask
from flask_restful import Api
from Device import Device 
from Room import Room 
from Home import Home

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8000))
print("Socket bound to " + sock.getsockname()[0])
sock.listen()
print("Server listening...")

def run():
    while True:
        connectionSocket, addr = sock.accept()
        print("CONNECTED SOURCE: " + str(addr))
        # connectionSocket.close()
        r = Home(True,True, 65)
        # r.leave_routine()

run()       
