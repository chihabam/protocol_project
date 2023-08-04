from Device import Device
class Light(Device):
        def __init__(self,stat, id,name):
            super().__init__(id,name)
            self.on= int(stat)
            self.set_status(stat)