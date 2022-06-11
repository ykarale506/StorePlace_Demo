# take a name from user

name = input("Whats your name : - ")

# take Maths, hostory and science ,marks

maths = input ("enter maths marks : - ")
science = input ("enter science marks: - ")
history = input ("enter history marks: - ")

sum = int(maths)+int(science)+int(history)
percent = int(sum/3)
print("Total marks is",sum)
print("and %  is ",percent)

