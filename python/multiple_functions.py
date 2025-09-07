class Multiplefunctions:
    def subfields(self):
        ai_fields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processin"]
        print("Sub-fields in AI are:")
        for sf in ai_fields:
            print(sf)

    def oddEvenFn(self):
        input_number = input("Enter Number to check odd or even:")
        try:
            number = int(input_number)
            if number % 2 != 0:
                print(f"{number} is odd")
            else:
                print(f"{number} is even")
        except ValueError:
            print("Invalid Input")

    def eligible(self):
        gender = input("Enter Gender:").lower()
        input_age = input("Enter Age:")
        try:
            age = int(input_age)
            if gender != "male" and gender != "female": 
                print("Invalid Gender")
            elif gender == "male" and  age >= 21:
                print("Eligible")
            elif gender == "female" and  age >= 18:
                print("Eligible")
            else:                
                print("Not Eligible")
        except ValueError:
            print("Invalid Input for Age")
        

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
