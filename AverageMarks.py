# Take input from User
maths = int(input("Please enter math marks : -  "))
english = int(input("Please enter english marks : -  "))
physics = int(input("Please enter physics marks : -  "))
chemestry = int(input("Please enter chemestry marks : -  "))
biology = int(input("Please enter biology marks : -  "))

average = (maths + english + physics + chemestry + biology) / 5

if (average >= 90):
    print("Your grade is  --  A and total % is " + str(average))

elif (average >= 80):
    print("Your grade is  --  B and total % is " + str(average))

elif (average >= 70):
    print("Your grade is  --  C and total % is " + str(average))

elif (average >= 60):
    print("Your grade is  --  D and total % is " + str(average))

elif (average >= 50):
    print("Your grade is  --  E and total % is " + str(average))

elif (average >= 40):
    print("Your grade is  --  F")
else:
    print("No Grade")