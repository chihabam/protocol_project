from http import HTTPStatus
from Home import Home
from PDU import Datagram




request=[Home]
home_out= Home(None,None,None)
data_out= Datagram(home_out)


def build_home():
    print("Please enter new id: ")
    id_sel= int(input())

def sel_home():
    print("Please enter existing home id: ")
    id_sel= int(input())
    print("Please enter device name: ")
    dev_name=str(input())
    print("What type of device is this? \n1. Light \n2. Thermostat \n3. Go Back")
    dev_type= int(input())
    if dev_type == 1:
            light_menu()
    elif dev_type== 2:
            thermostat_menu()
    elif dev_type== 3:  
            menu()
        
# def therm_ops(dir,value, diff):
#      if(dir == 1):
#           return value + diff
#      elif dir== 2:
#           return value - diff
        
     
def thermostat_menu():
    print("What do you want to change the temperature to in Farenheit?")
    choice = int(input())
    print("Changing temperature to ", choice)
def light_menu():
    print("What would you like to do the light? \n1. Turn off \n2. Turn On\n3. Do nothing")
    sel= int(input())
    if(sel==1 or sel ==2):
        print("request sent")

def menu(val):
    #Val is technically optoinal but allows outer methods force menu optoin if needed
    done = False
    sel= None
    while sel!=3 :
        print("Please select a menu action: \n1. Select home\n2. Build a home\n3. Leave")
        sel=int(input())
        if sel==1:
            sel_home()
        elif(sel ==2 ):
            build_home()
        elif(sel==3):
            print("Ending session")
menu(None)

    
    
        
