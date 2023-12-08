# import sys

# class Customer:
#     bank = "SBI"
    
#     def __init__(self,name,balance = 0.0):
#         self.name = name
#         self.balance = balance

#     def Deposit(self,Amount):
#         self.balance = self.balance + Amount
#         print("Balance After Deposit",self.balance)

#     def Withdraw(self,Amount):
#         if Amount > self.balance:
#             print("Insufficient Balance")
#             sys.exit()
#         self.balance = self.balance-Amount 
#         print("Balance After Withdraw",self.balance)
        
# print("Welcome to",Customer.bank)
# name = input("Enter Your Name : ")
# c=Customer(name)

# while True:
#     print("1-Deposit \n2-Withdraw \n3-Exit \n4-continue\n5-Exit")
#     option = int(input("Enter Your Option "))
#     if option == 1:
#         Amount = int(input("Enter the amount to Deposit "))
#         c.Deposit(Amount)
#         # print('Thank You for deposit')
#         # sys.exit()
#         # option = int(input("Enter Your Option "))
#         # if option == 5:
#         #     print(sys.exit())
#     elif option == 2:
#         Amount = int(input("Enter the amount to Withdraw "))
#         if(Amount ==100 or Amount == 500 or Amount== 1000):
#             c.Withdraw(Amount)
#         else:
#             print("This Amount cannot be withdraw")    

#     elif option == 3:
#         print(" Thankyou for Banking ") 
#         sys.exit()

#     else:
#         print(" Invalid option Entered ")       