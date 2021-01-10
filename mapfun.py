# predefined function
# needs two arguments - function and iterable
# repeats function for each element in the iterable
# returns the result of the function for each item of iterable and stores as list

def square(x):
    return x*x

numbers = [1,2,3,4,5]

listsqaures = map(square,numbers)

print(list(listsqaures))