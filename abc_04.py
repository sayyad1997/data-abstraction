from abc import ABC,abstractmethod

class SUBJECT(ABC):
    name="afroz"
    print(f"name of the student {name}")
    def subject(self):
        pass
    def marks(self):
        pass 

class MATHS(SUBJECT):
    def subject(self):
        print("subject is MATHS")
    def marks(self,mark):
        if mark<35:
            print(f"marks scored :{mark},progress of the student failed")
        elif mark>35 and mark<45:
            print(f"marks scored :{mark},progress of the student improve yourself")
        elif mark>45 and mark<65:
            print(f"marks scored :{mark},progress of the student good")
        elif mark>65 and mark<85:
            print(f"marks scored :{mark},progress of the student very good")
        else :
            print(f"marks scored :{mark},progress of the student excellent")

class  SCIENCE(SUBJECT):
    def subject(self):
        print("subject is SCIENCE")
    def marks(self,mark):
        if mark<35:
            print(f"marks scored :{mark},progress of the student failed")
        elif mark>35 and mark<45:
            print(f"marks scored :{mark},progress of the student improve yourself")
        elif mark>45 and mark<65:
            print(f"marks scored :{mark},progress of the student good")
        elif mark>65 and mark<85:
            print(f"marks scored :{mark},progress of the student very good")
        else :
            print(f"marks scored :{mark},progress of the student excellent")
class SOCIAL(SUBJECT):
    def subject(self):
        print("subject is SOCIAL")
    def marks(self,mark):
        if mark<35:
            print(f"marks scored :{mark},progress of the student failed")
        elif mark>35 and mark<45:
            print(f"marks scored :{mark},progress of the student improve yourself")
        elif mark>45 and mark<65:
            print(f"marks scored :{mark},progress of the student good")
        elif mark>65 and mark<85:
            print(f"marks scored :{mark},progress of the student very good")
        else :
            print(f"marks scored :{mark},progress of the student excellent")
class  ENGLISH(SUBJECT):
    def subject(self):
        print("subject is SOCIAL")
    def marks(self,mark):
        if mark<35:
            print(f"marks scored :{mark},progress of the student failed")
        elif mark>35 and mark<45:
            print(f"marks scored :{mark},progress of the student improve yourself")
        elif mark>45 and mark<65:
            print(f"marks scored :{mark},progress of the student good")
        elif mark>65 and mark<85:
            print(f"marks scored :{mark},progress of the student very good")
        else :
            print(f"marks scored :{mark},progress of the student excellent")

subject=SUBJECT()
math=MATHS()
science=SCIENCE()
social=SOCIAL()
english=ENGLISH()

math.subject()
math.marks(56)
science.subject()
science.marks(87)
social.subject()
social.marks(34)
english.subject()
english.marks(98)

