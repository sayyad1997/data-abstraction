from abc import ABC, abstractmethod

class VEHICLE(ABC):
    def display(self,name,model,type,milage):
        pass
class TATA(VEHICLE):
    def display(self,name):
        print(f"name of the company {name}")

class TATA_MODEL(VEHICLE):
    def display(self,model):
        print(f"model of vehicle {model}")

class TATA_TYPE(VEHICLE):
    def display(self,type):
        print(f"type of the vehicle {type}")

class TATA_MILAGE(VEHICLE):
    def display (self,milage):
        print(f"milage of the vehicle {milage}")

tata=TATA()
Model=TATA_MODEL()
Type=TATA_TYPE()
Milage=TATA_MILAGE()

tata.display("TATA")
Model.display("RFEG")
Type.display("PETROL")
Milage.display("23KM PER HOUR")