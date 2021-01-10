import os    #for removing the file

#f = open('trial.txt','r')          #file opened in read mode
#print(f.read())  #for reading whole file

#print(f.read(3))  #for reading certain amount of characters

#print(f.readline())  # for reading line 1
#print(f.readline())  # for reading line 2
#print(f.readline(5))  # for reading line 3 with only first 5 characters

#for x in f:
   # print(x)        #printing one line after another

#f.close()           #closing the file


#f = open('trial.txt','a')           #append mode...adding at the end of the file
#f.write('A new line now')
#f.close()

#f = open('trial.txt','w')           #write mode...overwriting the file
#f.write('A new line now')
#f.close()

#f = open('newfileee.txt','w')             #create mode...opening new file....use x or w

#os.remove('new.txt')

#if os.path.exists('newfileee.txt'):
 #   os.remove('newfileee.txt')
#else:
 #   print('File not present')

os.remove('trial.txt')