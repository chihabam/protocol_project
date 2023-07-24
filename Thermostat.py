class Thermostat(Device):
    def __init__(self, temp):
        self.status= temp
    def get_status(self):
        return self.status
    def set_status(self,temp):
        self.status=temp
            if(temp==false){
                self.status = 60
            }