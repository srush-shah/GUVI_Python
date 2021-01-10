# filter function takes in two arguments as its parameters where one is a function and the other is a list
# it returns a list of elements with result of boolean value true for each item in the list as per the criteria of the passed function

def prime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True


filtered = filter(prime,range(10))

print('Prime numbers are: ', list(filtered))