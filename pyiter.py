#tuple1 = ("car","bike","train")
#tuple2 = "apples"

#myit1 = iter(tuple1)
#myit2 = iter(tuple2)

#print(next(myit1))
#print(next(myit1))
#print(next(myit1))


#print(next(myit2))
#print(next(myit2))
#print(next(myit2))
#print(next(myit2))
#print(next(myit2))
#print(next(myit2))

#for x in tuple1:
#    print(x)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x




myclass = MyNumbers()

myiter = iter(myclass)


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))