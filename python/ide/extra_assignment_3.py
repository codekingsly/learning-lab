inp_num = input("value:")
try:
    num = int(inp_num)
    if(num == 10):
        print("CORRECT")
except ValueError:
    print("Invalid Number")
print("")

inp_pass = input("Enter the password:")
if(inp_pass == "HOPE@123"):
    print("Your password is correct")
else:
    print("Your password is incorrect")
print("")

inp_age = input("Age:")
try:
    age = int(inp_age)
    if age < 18:
        print("Children")
    elif age < 40:
        print("Adult")
    elif age < 60:
        print("Citizen")
    else:
        print("Senior Citizen")
except ValueError:
    print("Enter Valid Age")
print("")

inp_num = input("Enter any number to check positive or negative:")
try:
    num = float(inp_num)
    if(num > 0):
        print("Num is positive")
    else:
        print("Num is negative")
except ValueError:
    print("Invalid Number")
print("")

inp_num = input("Enter a number to check divisible by 5:")
try:
    num = float(inp_num)
    if num % 5 == 0:
        print(f"{inp_num} is divisible by 5")
    else:
        print(f"{inp_num} is not divisible by 5")
except ValueError:
    print("Invalid Number")