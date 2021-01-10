# Package

#NumPy
#Pendulum
#Python Imaging Library
#MoviePy
#Requests
#Tkinter
#PyQt
#Pandas
#py32
#pyTest
#mysql-connector
#mysql-connector-python
#inflect : for printing numbers as words

import camelcase  # Downloaded using the command "py -m pip install camelcase". Other libraries can be dwonloaded in the same way.

x = camelcase.CamelCase()

a = "hi there! this is a message to check if the letters of each word are capitalized"

print(x.hump(a))

# To remove a package use the following command in command prompt
# py -m pip uninstall camelcase

# To check the list of packages present
# py -m pip list