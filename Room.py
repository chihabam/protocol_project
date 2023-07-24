import Light from Light
import Thermostat from Thermostat
class Room:
    def __init__(self,f, k,temp):
        self.fr=Light(f)
        self.k= Light(k)
        self.t=Thermostat(temp)
        devices= [fr, k, t]
    def leave_routine():
        for x in devices:
            x.set_status(false)

        
