#Checking the condition of age
age = int(input("what your age?"))

if (age <= 4):
    print("you are baby!")
elif (age > 4) and (age < 12):
    print("you are kid")
elif (age >= 12) and (age < 30):
    print("you are teenager")
else:
    print("you are old")

