# print(10/2)
# print(10/0) #zero division error
# print(10/'zero')#--- Type Error

# a = int(input('en'))
# print(a) #---- Value Error if we given in string

# import math
# num = int(input("Enter the input  "))
# try:
#     result = math.factorial(num)
#     print(result)

# except:
#     print("Please do not enter Negative Numbers")   

# try:
#     num = int(input("input :  "))
#     if num <=0:
#         raise NameError("please enter +ve num")
# except NameError as error:
#     print(error)            

# finally:
#     print("goodbye")


# def addNum(num1,num2):
#     try:
#         print(num1+num2)
#     except TypeError:
#         print("Please enter integer values")    
#     except NameError:
#         print('Incorrect Parameters')   
#     except Exception as e:
#         print(e)   

# (addNum(1,9))
# print("The End...")

# try:
#     print(10/0)
# except BaseException:
#     print("Aman")
# print("outside try & Except block")    

# try:
#     print(10/0)
# except ArithmeticError:
#     print("Aman")
# print("outside try & Except block")   

# try:
#     print(10/0)
# except NameError:
#     print("Aman")
# print("outside try & Except block")   

# try:
#     print(10/2) # statement -1
#     print(10/0) # statement -2   Abnormal Termnination
#     print(10/5) # statement -3

# except ZeroDivisionError:
#     print("heyy") # statement -4

# print("How are yuhh")  # statement -5  


# try:
#     print(10/2) # statement -1
#     print(10/0) # statement -2   Normal Termination
#     print(10/5) # statement -3

# except ZeroDivisionError:
#     print("heyy") # statement -4

# print("How are yuhh")  # statement -5  

# try:
#     print(10/2) # statement -1  
#     print(10/0) # statement -2 Abnormal Termination
#     print(10/5) # print("How are yuhh")  # statement -5
# statement -3

# except ZeroDivisionError:
#     print(100/0) # statement -4


# try:
#     print(round(10/2))
#     print(10/0)

# except ValueError:
#     print("Give correct value")

# except ZeroDivisionError:
#     print("Error Found")    

# try:
#     print(round(10/2))
#     print(10/'a')
#     print(10/0)
  

# except TypeError:
#     print("Give correct value")

# except ZeroDivisionError as k: # to know the error by Aliasing
#     print("Error Found",k)  

# print("heyy bruhh")

# try:
#     print("SALAAR")
#     print(10/2)
#     print(10/'a')

# except TypeError:
#     print("Find Error")

# finally:
#     print("Print Anytime")    


# try:
#     print("SALAAR")
#     print(10/2)
#     print(10/0)

# except ZeroDivisionError:
#     print("Find Error")

# finally:
#     print("Print Anytime")   

