
# abc -> Module
# ABC -> BAse class

from abc import ABC, abstractmethod;

# class Help4Code(ABC):
#     @abstractmethod
#     def training(self):
#         pass
    
#     @abstractmethod
#     def placement(self):
#         pass

# class educator1(Help4Code):
#     def training(self):
#         print("Teach Pyhton, C++ Java  ")
    
#     def placement(self):
#         print("100% placement for JAVA Full Stack...");


# class educator2(Help4Code):
#     def training(self):
#         print("Teach Ruby, JavaScript, React");

#     def placement(self):
#         print("Full Stack developer")


# class educator3(Help4Code):
#     def training(self):
#         print("Teach MERN STACK");
    
#     def placement(self):
#         print("MERN Stack Development")

# e1 = educator1();
# e2 = educator2();
# e3 = educator3()

# print("----------------- Educator 1 ------------------------")
# e1.training();
# e1.placement();
# print()

# print("----------------- Educator 2 ------------------------")
# e2.training();
# e2.placement();

# print()
# print("----------------- Educator 2 ------------------------")

# e3.training();
# e3.placement();


# Example 1 

# class Irctc(ABC):
#     @abstractmethod 

#     def bookTicket(self):
#         pass

# class Bus(Irctc):
#     def bookTicket(self):
#         print("Booking for Bus Ticket - Pune to Nashik ");

# class MakeMyTrip(Irctc):

#     def bookTicket(self):
#         print("==================================================");
#         print("Welcome to MakeMyTrip!")

#         self.source = input("Enter a source name : ");
#         self.destination = input("Enter a destination name: ")
#         self.date = input("ENter Date ");
#         print("============================================")
    
#     def displayRecord(self):
#         print("Source = ", self.source);
#         print("destination = ", self.destination);
#         print("date = ", self.date);

# class GobiBo(Irctc):
#     def bookTicket(self):
#         print("=========================================")
#         print("Welcome to GobiBO!!");
    

# while True:
#     print("Press 1 for MakeMyTrip ")
#     print("Press 2 for GobiBo")
#     print("Press 3 for Exit")
#     choice = int(input("Select your application "))

#     match choice:
#         case 1:
#             m1 = MakeMyTrip();
#             m1.bookTicket();
#             print("------------- Record -----------------")
#             m1.displayRecord();
#             print()
            

#         case 2:
#             g1 = GobiBo();
#             print("------------- Record -----------------")
#             g1.bookTicket();
#             print()


#         case 3:
#             break;

#         case _:
#             print("No Application Present ")


# Chatgpt : search 
# class Arithmatic:
#     def add(self, a=0):
#         print(a)
    
#     def add(self, a=0, b=0):
#         print(a+b);
    
#     def add(self, a=0, b=0, c=0):
#         print(a+b+c);

# obj = Arithmatic();
# obj.add(10);
# obj.add(10, 20);
# obj.add(10, 30, 30);

# Constructor overloading 

# class Arithmatic:
#     def __init__(self, a=0):
#         print(a)
    
#     def __init__(self, a=0, b=0):
#         print(a+b);
    
#     def __init__(self, a=0, b=0, c=0):
#         print(a+b+c);

# obj = Arithmatic(10);
# obj = Arithmatic(10, 20);
# obj = Arithmatic(10, 20, 30);


# class Base:
#     def show(self):
#         print("Base class");
    

# class Derived(Base):
#     def show(self):
#         # super().show();
#         print("DErived class");

    
# D1 = Derived();

# D1.show();


# Method overriding

# class Rbi:
#     def homeLoan(self):
#         print("Home loan Rate of Interest 8%")

#     def carLoan(self):
#         print("Car loan Rate of Interest 7%")

# class Sbi(Rbi):
#     def homeLoan(self):
#         super().homeLoan(); 
#         print("Home loan Rate of Interest 10.6%")
    

# sbi = Sbi();
# sbi.homeLoan();
# sbi.carLoan();
        
# Constructor overriding  

# class father:
#     def __init__(self):
#         print("Father:- I am on time at breakfast table")
    
# class child(father):
#     def __init__(self):
#         super().__init__();
#         print("Child:- I will be late for breakfast")

# ch1 = child();

