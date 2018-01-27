# Index:  0      1         2        3        4
cars = ('bmw', 'seat', 'nissan', 'skoda', 'honda')

# Build a loop that takes the list and places it in variable X
# and then turns the entire list into uppercase letters
for x in cars:
    print(x.upper())

#this will print 1-5
for x in range(1, 6):
    print(x)

#this will print list of numbers, 0-10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mynumberl_list = list(range(0, 11))
print(mynumberl_list)

#This will print the list of numbers in increments of 2
for x in mynumberl_list:
    x = x * 2
    print(x)

