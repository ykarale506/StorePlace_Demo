# Print factorial number

x=int(input("Please enter your number :  - "))

a=0
b=1
print(a)
print(b)
while((a+b) < x):
     b=a+b
     a=b-a
     print(b)