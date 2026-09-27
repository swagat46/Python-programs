# custom exception program
#1. Custom Exception for Invalid Age
class InvalidAgeError(Exception):
    pass

#2. Custom Exception for Insufficient Balance
class InsufficientBalanceError(Exception):
    pass

#3.Custom Exception for Invalid Marks
class InvalidMarksError(Exception):
    pass

#4.Custom Exception for Invalid Password
class InvalidPasswordError(Exception):
    pass

#5.Custom Exception for Invalid Number
class InvalidNumberError(Exception):
    pass

try:
    # Age Validation
    age=int(input("Enter your age: "))
    if age<18:
        raise InvalidAgeError("Age must be 18 or above")
    print("Age is valid")

    #Bank balance validation

    balance=5000
    withdraw=int(input("Enter withdraw amount"))

    if withdraw >balance :
      raise InsufficientBalanceError("Insufficient bank balance.") 

    print("Withdrawal successful.")

    #marks validation
    marks=int(input("Enter marks:"))
    if marks< 0 or marks >100:
        raise InvalidMarksError("Marks must berween 0 and 100")
    print("Marks are valid")

    #Password Validation
    password=input("Enter password:")

    if len(password)<8:
        raise InvalidPasswordError("Password must contain at least 8 characters.")
    print("Password is valid.")

    #Number Validation
    number=int(input("Enter a positive number:"))

    if number<=0:
        raise InvalidNumberError("Number must be greater than zero.")
    print("Number is valid.")

except InvalidAgeError as e:
    print("Inavalid Age:",e)

except InsufficientBalanceError as e:
    print("Balance Error:",e)

except InvalidMarksError as e:
    print("Marks Error:",e)

except InvalidPasswordError as e:
    print("Password Error:",e) 

except InvalidNumberError as e:
    print("Number Error:",e)

finally:
    print("Program execution completed.")                   

