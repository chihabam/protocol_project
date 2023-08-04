from Device import Device

class Thermostat(Device):
    def __init__(self,id,name,temp):
        super().__init__(id,name)
        self.status= temp
    def get_status(self):
        return self.status
    def set_status(self,temp):
        self.status=temp
        if(temp==False):
            self.status = 60
        