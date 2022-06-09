# Office hrs practice

users = [
    {
    'first_name': 'neal',
    'last_name': 'dreessen',
    'age': 53,
    'email': 'neal@email.com'
    },
    {
    'first_name': 'burt',
    'last_name': 'reynolds',
    'age': 75,
    'email': 'burt@reynolds.com'
    },
    {
    'first_name': 'saul',
    'last_name': 'goodman',
    'age': 57,
    'email': 'saul@goodman.com'
    }
]

def iterateDictionary(lst):
    
    for i in range(0, len(lst)):
        str = ""
        for key, value in lst[i].items(): 
            str = str + f"{key} - {value}, "
        print(str)

iterateDictionary(users)

for value in users:
    print(value)

