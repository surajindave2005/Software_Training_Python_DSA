# class Base:
#     def __init__(self):
#         print("Parent class constructor called");
#         self.a = "Suraj"; # public Data
#         self.__c = "Darshan"; # private Data
    

# class Derived(Base):
#     def __init__(self):
#         super().__init__();
#         print("Calling private member of base class: ")
#         # print(self.a);
#         # print(self.__c);

# # obj1 = Derived();
# # print(obj1.a);
# # print(obj1.__c)

# obj2 = Base();
# # print(obj2.a); # Accessible 
# # print(obj2.__c); # Not Accessible 

# # # Protected
# class Base:
#     def __init__(self):
#         print("Parent class constructor called");
#         self.a = "Suraj"; # public Data
#         self._c = "Darshan"; # private Data
    

# class Derived(Base):
#     def __init__(self):
#         super().__init__();
#         print("Calling private member of base class: ")
#         print(self.a);
#         print(self._c);

# # obj1 = Derived();
# # print(obj1.a);
# # print(obj1._c)

# obj2 = Base();
# print(obj2.a); # Accessible 
# print(obj2._c); # Not Accessible 


# import mymodule;


# obj1 = mymodule.Derived();
# print(obj1.a);
# print(obj1._c)

# obj2 = mymodule.Base();
# print(obj2.a); # Accessible 
# print(obj2._c); # Not Accessible 

# protected

class Rbi:
    def publicPolicy(self):
        print("Check the public policy of RBI");
    
    def __privatePolicy(self):
        print("There is some private policy which is not accssibel for public");

class sbi(Rbi):
    def __init__(self):
        Rbi.__init__(self)
    
    def callingPublicMethod(self):
        print("\nInside child class");
        self.publicPolicy();
    
    def callingPrivateMethod(self):
        self.__privatePolicy();

obj1 = sbi();
# obj1.callingPublicMethod()
# print("------------------------------------------")
# obj1.callingPrivateMethod();
# print("------------------------------------------")
# obj1.publicPolicy()
# # print("------------------------------------------")
# obj1.__privatePolicy();


# obj2 = Rbi();
# print("------------------------------------------")
# obj2.publicPolicy();
# print("------------------------------------------")
# obj2.__privatePolicy();

