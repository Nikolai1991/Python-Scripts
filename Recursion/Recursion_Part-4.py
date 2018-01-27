# Fibonachi 0,1,1,2,3,5,8,13,21,34,55
def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
print(fibo(10))
# Fibonachi 0,1,1,2,3,5,8,13,21,34,55
