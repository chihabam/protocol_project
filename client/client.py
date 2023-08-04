from http import HTTPStatus
from Home import Home
from PDU import Datagram
import socket
import sys
import time



sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port= 8030
ip="0.0.0.0"

try:
     if(sys.argv[1]!=None):
         ip = sys.argv[1]
except:
    print("Destination IP address not entered.\n...\nSwitching to default IP")
sock.connect((str(ip),port))



class Request:

    def __init__(self):
         self.home= Home(0,0,0)
         self.pdu=Datagram(self.home)
         
    def build_home(self):
        print("Building feature not yet available")
        # id_sel= int(input())
        # t_str= self.pdu.toString()
        # clone =Datagram.decode_str(t_str)



    def sel_home(self):
        self.pdu.set_home(1,1)
        print("Please enter device name: ")
        dev_name=str(input())
        print("What type of device is this? \n1. Light \n2. Thermostat \n3. Go Back")
        dev_type= int(input())
        self.pdu.set_device(dev_type,dev_name,19265+self.pdu.seq_num)
        if dev_type == 1:
                self.light_menu()
        elif dev_type== 2:
                self.thermostat_menu()
        elif dev_type== 3:  
                menu(None)   
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
        sel= int(input()) -1
        self.pdu.set_operation(0,1,sel)
        command = str(self.pdu.toString())
        self.send_rq(str(command))
        clone =self.pdu.decode_str(str(command))
        
    
    def send_rq(self,str_cmd):
        print("Sending Packet: ", self.pdu.seq_num)
        sock.send(str(str_cmd).encode())
        print("Done Sending")
        response = sock.recv(1024).decode()
        if (response):
            self.pdu.seq_num= self.pdu.seq_num
            print("Server response:", response)
        sock.close()

    def print_pdu(self):
         print (self)
    

def get_home(h_id=1):
     home_id=h_id

def get_all_homes():
     print(1)

def menu(val):
    #Val is technically optoinal but allows outer methods force menu optoin if needed
    done = False
    sel= None
    resp_num=0
    while sel!=3 :
        req= Request()
        req.pdu.set_ports(port,ip)
        resp_num=0
        print("\n------- Menu ------- \n1. Select home\n2. Build a home\n3. Leave")
        sel=int(input())
        if sel==1:
            req.pdu.set_msg_flags(1,0)
            req.sel_home()
        elif(sel ==2 ):
            req.build_home()
        elif(sel==3):
             print(1)
        elif (sel==4):
            print("Ending session")
menu(None)

    
    
        
