import socket
from flask import Flask
from flask_restful import Api
from Device import Device 
from Room import Room 
from Home import Home
from PDU import Datagram
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8030))
print("Socket bound to " + sock.getsockname()[0])
sock.listen()
print("Server listening...")

home = Home(0,0,25)

def client_handler(c_socket):
    while True:
        data = c_socket.recv(1024).decode().strip()
        if not data:
            break
        response= "Received data:"
        print(response, data)
        pdu_in= Datagram(home)
        pdu_in.decode_str(data)
        print("Pdu d type", str(pdu_in.d_type))
        print(pdu_in.d_name)
        print(home.fr.name)
        type = int(pdu_in.d_type)
        if type==1:
            if (str(pdu_in.d_name)==str(home.fr.name)):
                print("Match Family Room")
                home.fr.status=pdu_in.payload
            elif (str(pdu_in.d_name)==str(home.k.name)):
                home.k.status=pdu_in.payload
        elif pdu_in.d_type==2:

            if str(pdu_in.d_name)==str(home.t.name):
                home.t.status= pdu_in.payload
        
        pdu_in.home.print_home()

        c_socket.send(response.encode())
    c_socket.close()

sock.listen(5)



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