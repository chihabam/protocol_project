from Light import Light 
from Thermostat import Thermostat 
class Home:
    tool =12
    def __init__(self,f, k, temp):
        self.fr=Light(int(f),12,"Family Home")
        self.k= Light(int(k),1,"Kitchen")
        self.t=Thermostat(13,"Thermostat",temp)
        self.h = 5 + Home.tool
        self.devices=[self.fr,self.k,self.t]
    def test(self):
        print(self.devices)

    def leave_routine(self):
        for x in self.devices:
            d_id=x.get_id()
            print("Deactivating Device at: " + str(d_id))
    def print_home(self):
            str_stat= ["Off", "On"] #this is used to conver boolean to string 
            print("\n---- Home Status ----"+"\n"+self.fr.name+" Light: "+str_stat[int(self.fr.get_status())] )
            print(str(self.k.name)+" Light: "+str_stat[int(self.k.get_status())] )
            print(self.t.name+" Temperature: "+str(self.t.get_status())+ "\n")
         
