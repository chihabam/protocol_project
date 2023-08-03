from http import HTTPStatus
from Home import Home
from PDU import Datagram
import socket


sock= socket.socket()
port= 8040
sock.connect(("",port))

class Request:

    def __init__(self):
         self.home= Home(0,0,0)
         self.pdu=Datagram(self.home)
         
    def build_home(self):
        print("Please enter new id: ")
        id_sel= int(input())



    def sel_home(self):
        print("Please enter existing home id: ")
        id_sel= int(input())
        self.pdu.set_home(1,id_sel)
        print("Please enter device name: ")
        dev_name=str(input())
        print("What type of device is this? \n1. Light \n2. Thermostat \n3. Go Back")
        dev_type= int(input())
        self.pdu.set_device(dev_type,dev_name,19245)
        if dev_type == 1:
                self.light_menu()
        elif dev_type== 2:
                self.thermostat_menu()
        elif dev_type== 3:  
                menu()   
    def thermostat_menu(self):
        print("What do you want to set the temperature to (Farenheit)?")
        choice = int(input())
        # request= self.pdu.toString()
        self.pdu.set_operation(0,1,choice)
        print("Changing temperature to ", choice)
        command = self.pdu.toString()
        print("Changing temperature to ", choice)
        print(command)
        self.send_rq(str(command))

    def light_menu(self):
        print("What would you like to do the light? \n1. Turn off \n2. Turn On\n3. Do nothing")
        sel= int(input())
        self.pdu.set_operation(0,1,sel)
        command = self.pdu.toString()
        print(command)
        self.send_rq(str(command))
    
    def send_rq(self,str_cmd):
        sock.send(str(str_cmd).encode())
        response = sock.recv(1024).decode()
        print("Server response:", response)

def menu(val):
    #Val is technically optoinal but allows outer methods force menu optoin if needed
    done = False
    sel= None
    req= Request()
    req.pdu.set_ports(None,port)
    resp_num=0
    while sel!=3 :
        print("Please select a menu action: \n1. Select home\n2. Build a home\n3. Leave")
        sel=int(input())
        if sel==1:
            req.pdu.set_msg_flags(1,0)
            req.sel_home()
        elif(sel ==2 ):
            req.build_home()
        elif(sel==3):
            print("Ending session")
menu(None)

    
    
        
