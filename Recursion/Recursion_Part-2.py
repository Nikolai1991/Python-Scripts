# Sum = 1+2+3+4+5 = 15
def sum(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + sum(x-1)

z = sum(5)
print(z)
# Sum = 1+2+3+4+5 = 15

