import sys

validPassword = '123456' #this is our password.

inputPassword = input('Please Enter Password: ')

if inputPassword == validPassword:
    print('You have access!')
else:
    print('Access denied!')
    sys.exit(0)

print('Welcome!')
