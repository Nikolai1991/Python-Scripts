# The following script arranges the list of numbers in the correct order

#Index      0   1   2   3   4   5  6
oldlist = [10, 75, 43, 15, 25, -4, 27]

def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for z in range(0, last_item):
        for x in range(0, last_item-z):
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]

    return mylist

print('Old List', oldlist)
newlist = bubble_sort(oldlist).copy()
print('New List: ', newlist)
