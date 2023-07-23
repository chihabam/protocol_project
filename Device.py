class Device:
    def __init__(self,status):
        self.status=bool #Where true is on and false is off
    def get_status(self):
        return self.status
    def set_status(self,status):
        self.on=status


