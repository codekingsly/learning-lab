print("Welcome to Assignment-1", "\n")

num1=10
print("Num1=", 10)
num2=10
print("Num1=", 10)
print("Add=", num1 + num2, "\n")

bmi_input  = input("Enter the BMI Index:")
try:
    bmi = float(bmi_input )
    if bmi < 18.5:
        print("Under Weight")
    elif bmi < 25:
        print("Normal Weight")
    elif bmi < 30:
        print("Over weight")
    else:
        print("Obesity")
except ValueError:
    print("Invalid Input")
