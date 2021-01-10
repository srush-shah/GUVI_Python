import pickle

mydict = {'1':'a','2':'b'}

pickle_file = open("picklefile.txt","wb")

pickle.dump(mydict,pickle_file)

pickle_file = open("picklefile.txt","rb")

new_dict = pickle.load(pickle_file)

print(new_dict)