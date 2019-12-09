class Customer:
    
    def __init__(self,firstName,lastName):
        self.__firstName:str = firstName
        self.__lastName:str = lastName

    def getFirstName(self) ->str:
        return self.__firstName
    
    def getLastName(self) ->str:
        return self.__lastName
    
    def setAccount(self,account):
        self.__account = Account(0)
    
    def getAccount(self):
        return self.__account
    
class Account:
    def __init__(self,balance:float):
        self.__balance == 0

    def getBalance(self) ->float:
        return self.__balance
    
    def deposit(self,amt:float) ->bool:
        if amt < 0:
            return False
        self.__balance += amt
    
    def withdraw(self,amt:float) ->bool:
        if amt> self.__balance:
            return False
        self.balance -= amt
    
class Bank:
    def __init__(self,bankName):
        self.__bankName = bankName
        self.__numberOfCustomers = 0
        self.__customers = []

    def addCustomer(self,firstName,lastName):
        self.__numberOfCustomers += 1
        self.__customers.append(firstName + " " + lastName)
        Customer(firstName,lastName)

    def getNumOfCustomers(self):
        return self.__numberOfCustomers
    
    def getCustomer(self,index):
        return self.__customers[index]

b = Bank("jo")
b.addCustomer("ha","la")
print(b.getNumOfCustomers())
print(b.getCustomer(0))

        