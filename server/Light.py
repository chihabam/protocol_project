from Device import Device
class Light(Device):
        def __init__(self, id,name):
            super().__init__(id,name)
            self.brightness= 60
            
