# Nested Dictionaries and Lists

print("\n1. Update values in Dictionaries and List:\n")

x = [[5, 2, 3], [10, 8, 9]]

students = [
    {'first_name': 'Michael', 'last_name': 'Jordon'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball': ['Kobe', 'Jordon', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

z = [
    {'x': 10, 'y': 20}
]

print("\n1.1 Change value 10 in x to 15.\n")
print(x)
x[1][0] = 15
print(x)

print("\n1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'\n")
print(students)
students[0]['last_name'] = 'Bryant'
print(students)

print("\n1.3 Change 'Messi' to 'Andres'\n")
print(sports_directory)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

print("\n1.4 Change the value 20 in z to 30\n")
print(z)
z[0]['y'] = 30
print(z)

print("\n2. Iterate Through a List of Dictionaries\n")

def iterateDictionary(lst):
    for i in range(0, len(lst)):
        for key, value in lst[i].items(): # ex. crash-course pg109
            print(f"{key} - {value}")
                
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

print(f"\nstudents = {students}\n")
iterateDictionary(students) 
print(f"\nz = {z}\n")
iterateDictionary(z)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

print("\n3. Get Values From a List of Dictionaries\n")

def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        print(some_list[i][key_name])

print(f"students = {students}\n")
iterateDictionary2('first_name', students)
print(f"\n")
iterateDictionary2('last_name', students)

print("\n4. Iterate Through a Dictionary with List Values\n")

def print_info(some_dict):
    for key in some_dict:
        print(f"\n{len(some_dict[key])} {key}")
        for value in some_dict[key]:
            print(value)

dojo = {
    'locations': [
        'San Jose',
        'Seattle',
        'Dallas',
        'Chicago',
        'Tulsa',
        'DC',
        'Burbank'],
    'instructors': [
        'Michael',
        'Amy',
        'Eduardo',
        'Josh',
        'Graham',
        'Patrick',
        'Minh',
        'Devon']
}

print_info(dojo)
