print("###### Update Values in Dicts and  lists ######")
x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
students[0]["last_name"] = "Bryant"
print(students)
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
z[0]["y"] = 30
print(z)

print("\n\n###### Iterate Through a list of dicts ######")
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(input_list):
	 for input in input_list:
	 	f_name = input["first_name"]
	 	l_name = input["last_name"]
	 	print("first_name -",f_name,", last_name -",l_name)

	
iterateDictionary(students)


print("\n\n######## Get Values form a list of Dicts #########")
def iterateDictionary2(key_name, some_list):
	for dict in some_list:
		print(dict[key_name])

iterateDictionary2('first_name', students)

print("\n\n######## Iterate Through a dict with list values ##########")
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
	for key, values in some_dict.items():
		print("\n",len(values),key)
		for value in values:
			print(value)
printInfo(dojo)

