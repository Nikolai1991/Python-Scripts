mynumberl_list = list(range(0, 11))
print(mynumberl_list)

#This will print the list of numbers in increments of 2
for x in mynumberl_list:
    x = x * 2
    print(x)

#Arrange the numbers from big to small
mynumberl_list.sort(reverse=True)
print(mynumberl_list)

#Selects the largest number in the list
print('Max Number is: ' + str(max(mynumberl_list)))

#Selects the smallest number in the list
print('Min Number is: ' + str(min(mynumberl_list)))

#Calculates the amount of the list
print('SUM of List is: ' + str(sum(mynumberl_list)))

