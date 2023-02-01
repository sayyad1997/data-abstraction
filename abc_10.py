from abc import ABC,abstractmethod

class HARSHA_SHOW_ROOM(ABC):
    item_name: str = " " 
    item_quantity : int
    item_price : int

    @abstractmethod
    def total_price(self):
        pass

class TATA(HARSHA_SHOW_ROOM):
    def __init__(self,name:str,quantity:int,price:int):
        self.item_name=name
        self.item_quantity=quantity
        self.item_price=price

    def total_price(self):
        total=self.item_quantity*self.item_price
        self.item_price=total+total*18/100
        return self.item_price

    def display(self):
        print(f"name of the car {self.item_name}")
        print(f"number of cars {self.item_quantity}")
        print(f"total price of cars including with gst 18% : {self.item_price}")

class TOYOTA(HARSHA_SHOW_ROOM):
    def __init__(self,name:str,quantity:int,price:int):
        self.item_name=name
        self.item_quantity=quantity
        self.item_price=price

    def total_price(self):
        total=self.item_price*self.item_quantity
        self.item_price=total+total*20/100
        return self.item_price

    def display(self):
        print(f"name of the car {self.item_name}")
        print(f"number of cars {self.item_quantity}")
        print(f"total price of cars including with gst 20% : {self.item_price}")


class PAYMENT:
    status:bool=False
    type:str=" "
    
    def total_payment(self,type):
        status=False
        if type=="UPI" or type=="CREDIT_CARD" or type=="DEBIT_CARD" or type=="CASH" :
            self.status=True
            print(f"transaction done through {type}")
            print("transaction successful")
            return self.status
        else:
            print("transaction canceled")
        return self.status

if __name__=="__main__":
    payment=PAYMENT()
    ord=TATA("SUG",5,1200000)
    ord.total_price()
    ord.display()
    ord=TOYOTA("XUV",4,1200000)
    ord.total_price()
    ord.display()
    payment.total_payment("CREDIT_CARD")
    if(payment.status):
        print("your Order has been placed")




