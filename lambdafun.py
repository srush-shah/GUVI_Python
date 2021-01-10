x = lambda a,b: a+b

print(x(5,30))


def f1(n):
    return lambda a: a*n

doub = f1(2) # doubler function created and lambda function stored in doub
trip = f1(3) # tripler function created and lambda function stored in trip

print(doub(3))
print(trip(3))

