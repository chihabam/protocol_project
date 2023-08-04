class Device:
    def __init__(self,id,name):
        self.status=True 
        self.name= name
        self.id= id
        #print("New Device: "+ str(id))
        #Where true is on and false is off
    def get_status(self):
        #return self.status
        return self.status
    def set_status(self,nstatus):
        self.status=nstatus

    def get_id(self):
        return self.id


