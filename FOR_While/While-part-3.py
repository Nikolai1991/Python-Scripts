my_list = []
msg = ''
while msg != 'stop'.upper():
    msg = input("Enter new item, for stopping the list enter, STOP: ")
    my_list.append(msg)

print(my_list)

