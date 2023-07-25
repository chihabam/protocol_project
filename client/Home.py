from Light import Light 
from Thermostat import Thermostat 
class Home:
    tool =12
    def __init__(self,f, k,temp):
        self.fr=Light(12,"Family Home")
        self.k= Light(1,"Kitchen")
        self.t=Thermostat(13,temp)
        self.h = 5 + Home.tool
        self.devices=[self.fr,self.k,self.t]
    def test(self):
        print(self.devices)

    def leave_routine(self):
        for x in self.devices:
            d_id=x.get_id()
            print("Deactivating Device at: " + str(d_id))

        
