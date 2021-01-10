import json

person = {"name": "Bob","age": 12, "languages": "English"}

#person_dict = json.loads(person)

#print(person_dict)
#print(person_dict['languages'])

with open("data.json") as f: # opening json file
    data = json.load(f)  # loading json file into data

#print(data)     # printing dictionary
print(json.dumps(data, indent=4, sort_keys=True)) # For displaying data in a better format
# True prints the data in ascending order of the keys and False prints it in the format as it is

# dictionary as a string file

#person_json = json.dumps(person)

#print(person_json)

# writing to a json file
#with open('person.txt','w') as json_file:
 #   json.dump(person,json_file)

'''
Only these types can be converted to json: 

dict
list
tuple
str
int
float
Bool
None

'''

