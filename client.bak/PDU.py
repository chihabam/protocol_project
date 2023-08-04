from Room import Room
from Home import Home
from flask import jsonify


class Datagram:
    seq=0
    def __init__(self,Home):
        self.Home= Home
        Datagram.seq= Datagram.seq+10
        self.seq_num=Datagram.seq
        #print("New Datagram", self.seq)

    def decode_str(self,string_in):
        #The decoder will parse elements one line at a time
        vals= str(string_in).split(" ")
        self.seq_num=vals[0]
        self.dPort= vals[1]
        self.dIP=vals[2]
        self.msg_type=vals[3]
        self.msg_resp_num=vals[4]
        self.home_op=vals[5]
        self.home_id=vals[6]
        self.d_type=vals[7]
        self.d_name=vals[8]
        self.d_id=vals[9]
        self.op_id=vals[10]
        self.op=vals[11]
        self.payload=vals[12]
        print("Decoded", vals)
    
    def set_ports(self,dest_p,dest_ip):
         self.dPort=dest_p
         self.dIP=dest_ip
         
    def set_msg_flags(self, type,resp_num):
        self.msg_type= type #0 is none, 1 is incoming 2 is outbound, 3 is response
        self.msg_resp_num= resp_num #left 0 unless coming from server
    def set_home(self, home_op, home_id ):
        self.home_op= home_op #For home op 1 is select and 2 is build a home
        self.home_id= home_id #home id is simply the id we will use to scan json
    def set_device(self,d_type,d_name,d_id):
        self.d_type= d_type #Device type 1 is light 2 is thermostat 3 is neither
        self.d_name=d_name #The device name
        self.d_id=d_id #the device ID
    
    def set_operation(self,op_id,op,payload):
        self.op_id= op_id #indiviual operation no longer needed
        self.op=op #0 id no operation, 1 is set a value, 2 is get a value, 3 is delete a value 2 is create
        self.payload=payload #payload is simply the data being sent whether if its a temperature, on, or off

    def toString(self):
        list = [self.seq_num,self.dPort,self.dIP,
                self.msg_type,self.msg_resp_num,
                self.home_op,self.home_id,self.d_type,self.d_name,
                self.d_id,self.op_id,self.op,self.payload]
        list_str= " ".join(str(i) for i in list)
        print("Items into a list_str", list_str)
        return list_str
    
    def toJSON(self):
        return list_str

