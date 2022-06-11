# Print Rectangle

num = input("Enter number - ")
num = int(num)

for i in range(1,11):
    count = num * i
    if(count%3!=0):
        print(count)

