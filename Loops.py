# take input from user

data = input("Enter number :")
data = float(data)

# check if number is -ve or 0 or +ve

if (data < 0):
    print("This is negative number")
elif (data > 0):
    if(data%2==0):
        print("This is Even number")
    else:
        print("This is odd number")
elif(data == 0):
        print("This is Zero")


