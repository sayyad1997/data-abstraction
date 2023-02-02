from abc import ABC,abstractmethod

class D_MART(ABC):
    item_name: str = " " 
    item_quantity : int
    item_price : int

    def total_price(self):
        if self.item_name=="grocery":
            total=self.item_quantity*self.item_price
            self.item_price=total+total*5/100
            return self.item_price
        elif self.item_name=="cloths":
            total=self.item_quantity*self.item_price
            self.item_price=total+total*8/100
            return self.item_price
        elif self.item_name=="chappals":
            total=self.item_quantity*self.item_price
            self.item_price=total+total*7/100
            return self.item_price
        elif self.item_name=="stationary":
            total=self.item_quantity*self.item_price
            self.item_price=total+total*4/100
            return self.item_price

class GROCERY(D_MART):
    def __init__(self,name:str,quantity:int,price:int):
        self.item_name=name
        self.item_quantity=quantity
        self.item_price=price

    def display(self):
        print(f"name of the item {self.item_name}")
        print(f"number of items {self.item_quantity}")
        print(f"total price of items including with gst 5% : {self.item_price}")

class CLOTHS(D_MART):
    def __init__(self,name:str,quantity:int,price:int):
        self.item_name=name
        self.item_quantity=quantity
        self.item_price=price

    def display(self):
        print(f"name of the item {self.item_name}")
        print(f"number of item {self.item_quantity}")
        print(f"total price of item including with gst 8% : {self.item_price}")

class STATIONARY(D_MART):
    def __init__(self,name:str,quantity:int,price:int):
        self.item_name=name
        self.item_quantity=quantity
        self.item_price=price

    def display(self):
        print(f"name of the item {self.item_name}")
        print(f"number of items {self.item_quantity}")
        print(f"total price of items including with gst 4% : {self.item_price}")

class CHAPPALS(D_MART):
    def __init__(self,name:str,quantity:int,price:int):
        self.item_name=name
        self.item_quantity=quantity
        self.item_price=price

    def display(self):
        print(f"name of the item {self.item_name}")
        print(f"number of items {self.item_quantity}")
        print(f"total price of items including with gst 7% : {self.item_price}")



class PAYMENT:
    status:bool=False
    type:str=" "
    
    def payment_type(self,type):
        status=False
        if type=="UPI" or type=="CREDIT_CARD" or type=="DEBIT_CARD" or type=="CASH" :
            self.status=True
            print("transaction successful")
            print(f"transaction done through {type}")
            return self.status
        else:
            print("transaction canceled")
        return self.status

if __name__=="__main__":
    payment=PAYMENT()
    gro=GROCERY("grocery",5,120)
    gro.total_price()
    gro.display()
    sta=STATIONARY("stationary",6,12)
    sta.total_price()
    sta.display()
    cha=CHAPPALS("chappals",2,540)
    cha.total_price()
    cha.display()
    clo=CLOTHS("cloths",6,2345)
    clo.total_price()
    clo.display()


    payment.payment_type("CREDIT_CARD")
    def total():
        total=gro.item_price+sta.item_price+cha.item_price+clo.item_price
        print(f"total amount paid for the purchased items : {total}")

    t=total()

    if(payment.status):
        print("your Order has been placed")

