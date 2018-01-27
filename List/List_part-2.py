#this will print list of numbers, 0-10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mynumberl_list = list(range(0, 11))
print(mynumberl_list)

# Index: -5     -4        -3       -2       -1
# Index:  0      1         2        3        4
cars = ('bmw', 'seat', 'nissan', 'skoda', 'honda')
#Cut out part of the list (1:4 means 1,2,3)
mycars = cars[1:4]
print(mycars)

#Print all without the last object, [:] means start from 0
mycars = cars[0:4]
print(mycars)

#print ('nissan', 'skoda')
mycars = cars[-3:-1]
print(mycars)
