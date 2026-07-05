
# Protected
class Base:
    def __init__(self):
        print("Parent class constructor called");
        self.a = "Suraj"; # public Data
        self._c = "Darshan"; # private Data
    

class Derived(Base):
    def __init__(self):
        super().__init__();
        print("Calling private member of base class: ")
        print(self.a);
        print(self._c);

# obj1 = Derived();
# print(obj1.a);
# print(obj1._c)

obj2 = Base();
print(obj2.a); # Accessible 
print(obj2._c); # Not Accessible 


