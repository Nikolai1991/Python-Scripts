def test(x):
    if x == 0:
        return
    else:
        print('Hello World!')
        test(x-1)
test(2) # will print 2 times 'Hello World'
