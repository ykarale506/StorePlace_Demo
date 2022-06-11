# Take 3 input from user
# Find largest number

num1 = input("Enter Number 1 : ")
#num1= int(num1)
num2 = input("Enter Number 2 : ")
#num2= int(num2)
num3 = input("Enter Number 3 : ")
#num3= int(num3)

if(int(num1) > int(num2)):
    if(int(num1) > int(num3)):
        print("Largest number is " + num1)
    else:
        print("Largest number is : " + num3)

elif(int(num1) < int(num2)):
    if(int(num2) > int(num3)):
        print("Largest number is : " + num2)
    else:
        print("Largest nuber is  : "+ num3)

