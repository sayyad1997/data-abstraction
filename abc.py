from abc import ABC,abstractmethod

class animal(ABC):
    def display(self,name,sound,type,breed):
        pass

class TIGER(animal):
    def display(self,name,sound):
        print(f"name of the animal : {name}")
        print(f"{name} will {sound}")



ani_mal=animal()
wild=TIGER()

wild.display("tiger","roar")