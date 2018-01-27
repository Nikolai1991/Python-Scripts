#while loop with input
message = ''

while True:
    message = input("Enter Password: ")
    if message == 'davidov':
        break
    else:
        print("Password Not Correct, Please try again:")

print("That's right:", message, 'is the Password!')
