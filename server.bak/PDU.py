from Room import Room

class Datagram:
    seq=0
    def __init__(self,Home):
        self.Home= Home
        Datagram.seq= Datagram.seq+1
        self.seq_num=Datagram.seq
        print
    def decode_str(self,string):
        #The decoder will parse elements one line at a time
        print("Decoded")
    
    