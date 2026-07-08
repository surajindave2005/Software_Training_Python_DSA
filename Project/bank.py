# - By Suraj Indave
# ==============================================
#        BANK ACCOUNT MANAGEMENT SYSTEM
# ==============================================

# Base Class
class BankAccount:

    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance      # Private Variable (Encapsulation)

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"\n₹{amount} Deposited Successfully.")
        else:
            print("\nInvalid Deposit Amount.")

    # Withdraw Method
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"\n₹{amount} Withdrawn Successfully.")
        else:
            print("\nInsufficient Balance!")

    # Balance Inquiry
    def check_balance(self):
        print(f"\nCurrent Balance : ₹{self.__balance:.2f}")

    # Getter Method
    def get_balance(self):
        return self.__balance

    # Setter Method
    def set_balance(self, balance):
        self.__balance = balance

    # Display Account Details
    def display_details(self):
        print("\n-------------------------------")
        print("Account Number :", self.account_number)
        print("Account Holder :", self.account_holder)
        print("Balance        : ₹", self.__balance)
        print("-------------------------------")


# ==============================================
# Savings Account Class
# ==============================================

class SavingsAccount(BankAccount):

    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest Added : ₹{interest:.2f}")


# ==============================================
# Current Account Class
# ==============================================

class CurrentAccount(BankAccount):

    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # Method Overriding (Polymorphism)
    def withdraw(self, amount):

        current_balance = self.get_balance()

        if amount > 0 and (current_balance - amount) >= -self.overdraft_limit:
            self.set_balance(current_balance - amount)
            print(f"\n₹{amount} Withdrawn Successfully.")
        else:
            print("\nWithdrawal exceeds Overdraft Limit!")


# ==============================================
# Main Program
# ==============================================

account = None

while True:

    print("\n===================================")
    print("   BANK ACCOUNT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Display Account Details")
    print("7. Add Interest (Savings Only)")
    print("8. Exit")

    choice = int(input("\nEnter Your Choice : "))

    if choice == 1:

        acc_no = input("Enter Account Number : ")
        holder = input("Enter Account Holder Name : ")
        balance = float(input("Enter Opening Balance : "))

        account = SavingsAccount(acc_no, holder, balance)

        print("\nSavings Account Created Successfully!")

    elif choice == 2:

        acc_no = input("Enter Account Number : ")
        holder = input("Enter Account Holder Name : ")
        balance = float(input("Enter Opening Balance : "))

        account = CurrentAccount(acc_no, holder, balance)

        print("\nCurrent Account Created Successfully!")

    elif choice == 3:

        if account:
            amount = float(input("Enter Deposit Amount : "))
            account.deposit(amount)
        else:
            print("\nPlease Create an Account First.")

    elif choice == 4:

        if account:
            amount = float(input("Enter Withdrawal Amount : "))
            account.withdraw(amount)
        else:
            print("\nPlease Create an Account First.")

    elif choice == 5:

        if account:
            account.check_balance()
        else:
            print("\nPlease Create an Account First.")

    elif choice == 6:

        if account:
            account.display_details()
        else:
            print("\nPlease Create an Account First.")

    elif choice == 7:

        if isinstance(account, SavingsAccount):
            account.add_interest()
        elif account:
            print("\nInterest is Available Only for Savings Account.")
        else:
            print("\nPlease Create an Account First.")

    elif choice == 8:

        print("\nThank You for Using Bank Account Management System.")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")