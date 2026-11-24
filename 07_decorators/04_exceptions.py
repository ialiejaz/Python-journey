# try:
#     numerator = int(input("enter numerator = "))
#     denominator = input("enter denominator = ")

#     result = numerator/denominator
#     print(result)
# except:
#     print(f"denominator can't be {type(denominator).__name__}!")



# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 1/num
#     print(reciprocal)

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("You cannot divide by zero!")

try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The requested file was not found.")
else:
    print("File read successfully.")
finally:
    print("Executing cleanup operations (e.g., closing resources).")

# def age_check(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     print(f"{age} is a valid age.")

# age_check(-1)

# class InsufficientFunds(Exception):
#     pass

# def Atm(amount,balance):
#     if amount > balance:
#         raise InsufficientFunds(f"The entered amount of Rs.{amount} is less than avaialable balance")
#     remaining_balance =  balance - amount
#     print(f"remaining balance: Rs.{remaining_balance}")
#     return remaining_balance

# try:
#     withdraw = Atm(200,500)
    

# except InsufficientFunds as e:
#     print(f"Transaction failed!: {e}")



# try:
#     x = int(input("Enter value:"))
#     if x > 5:
#         result = 765/x
#         print(result)
        
# except ValueError:
#     print("Invalid entry!")
    
# except ZeroDivisionError:
#     print("Invalid entry!")