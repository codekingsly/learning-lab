#1
class SubfieldsInAI:
    def subfields(self):
        ai_fields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processin"]
        for sf in ai_fields:
            print(sf)

print("Sub-fields in AI are:")
subfieldsInAIObj = SubfieldsInAI()
subfieldsInAIObj.subfields()
print("")

#2
class OddEven:
    def oddEvenFn(self, num):
        if num%2 != 0:
            print(f"{num} is odd")
        else:
            print(f"{num} is even")

input_number = input("Enter Number to check odd or even:")
try:
    number = int(input_number)
    oddEvenObj = OddEven()
    oddEvenObj.oddEvenFn(number)
except ValueError:
    print("Invalid Input")
print("")

#3
class EligibilityForMarriage:
    def eligible(self, gender, age):
        if gender != "male" and gender != "female": 
            print("Invalid Gender")
        elif gender == "male" and age >= 21:            
            print("Eligible")
        elif gender == "female" and age >= 18:            
            print("Eligible")
        else:            
            print("Not Eligible")

input_gender = input("Enter Gender:").lower()
input_age = input("Enter Age:")
try:
    age = int(input_age)
    eligibilityForMarriageObj = EligibilityForMarriage()
    eligibilityForMarriageObj.eligible(input_gender,age)
except ValueError:
    print("Invalid Input for Age")
print("")

#4
class FindPercent:
    def percentage(self):
        input_no_of_sub = input("Enter Number of subjects:")
        try:
            no_of_sub = int(input_no_of_sub)
            total_marks = 0
            for nos in range(no_of_sub):
                mark_subject = int(input(f"Subject{nos+1}="))
                total_marks= total_marks + mark_subject    
            print("Total:", total_marks)
            print("Percentage:", (total_marks/(100*no_of_sub)) * 100)
        except:
            print("Invalid Input for Subjects or Marks")       

findPercentObj = FindPercent()
findPercentObj.percentage()
print("")

#5
class Triangle:
    def triangle(self):
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", (height*breadth)/2)

        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", height1+height2+breadth)

triangleObj = Triangle()
triangleObj.triangle()
print("")
