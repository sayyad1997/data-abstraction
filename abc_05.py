from abc import ABC,abstractmethod

class VEHICLE(ABC):
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost

    def model(self):
        pass 

    def price(self):
        pass

class TATA(VEHICLE):
    def __init__(self,name,cost):
        super().__init__(name,cost)
    def model(self):
        print(f"company of the vehicle {self.name}")
        x=["XET","DEE","DRE","TRFR"]
        print(f"models in {self.name} are :")
        for i in x:
            print(i)
    def price(self):
        x=["XET","DEE","DRE","TRFR"]
        for i in x:
            if i =="XET":
                print(f"model of the car :{i}")
                self.cost+=self.cost*12/100
                print(f"cost of the car {self.cost}")

            elif i=="DEE":
                print(f"model of the car :{i}")
                self.cost+=self.cost*14/100
                print(f"cost of the car {self.cost}")

            elif i=="DRE":
                print(f"model of the car :{i}")
                self.cost+=self.cost*16/100
                print(f"cost of the car {self.cost}")

            else:
                print(f"model of the car :{i}")
                self.cost+=self.cost*18/100
                print(f"cost of the car {self.cost}")

class MAHINDRA (VEHICLE):
    def __init__(self,name,cost):
        super().__init__(name,cost)

    def model(self):
        print(f"company of the vehicle {self.name}")
        x=["SAS","DEF","FR","DFE"]
        print(f"models in {self.name} are :")
        for i in x:
            print(i)
    def price(self):
        x=["SAS","DEF","FR","DFE"]
        for i in x:
            if i =="SAS":
                print(f"model of the car :{i}")
                self.cost+=self.cost*(13/100)
                print(f"cost of the car {self.cost}")

            elif i=="DEF":
                print(f"model of the car :{i}")
                self.cost+=self.cost*15/100
                print(f"cost of the car {self.cost}")

            elif i=="FR":
                print(f"model of the car :{i}")
                self.cost+=self.cost*17/100
                print(f"cost of the car {self.cost}")

            else:
                print(f"model of the car :{i}")
                self.cost+=self.cost*19/100
                print(f"cost of the car {self.cost}")


tata=TATA("tata",1200000)
mahi=MAHINDRA("mahindra",1200000)

tata.model()
tata.price()
mahi.model()
mahi.price()