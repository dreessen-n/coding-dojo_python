"""
Logging is tracking events as the software runs
I don't see one other than print statements through out file
"""
num1 = 42 # Variable declaration
num2 = 2.3 # Data type: float number
boolean = True # Data type: boolena
string = 'Hello World' # Data type: string

# pizza_toppings is a list, initialize list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# person is an dictionary, initialize dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# fruit is a tuple, initialize tuple
fruit = ('blueberry', 'strawberry', 'banana')

print(type(fruit)) # type check

print(pizza_toppings[1]) # Access list value in index 1
pizza_toppings.append('Mushrooms') # Add value to list

print(person['name']) # Print key for dict person
person['name'] = 'George' # Add key and value to dict person
person['eye_color'] = 'blue' # Add key and value to dict person

print(fruit[2]) # Access value of tuple
# Tuple values can not change, unless you reinitialize whole tuple

# Below is an if-else statement
if num1 > 45: # Start of if statement, if num1 is greater than 45, run
    print("It's greater") # Print if num1 is greater than 45
else: # Else statment to run if above is false
    print("It's lower") # Print is num1 is less than 45

# Belwo is an if-elif-else statement
if len(string) < 5: # Length check, if length of string less than 5
    print("It's a short word!") # Print if string less than 5
elif len(string) > 15: # If string length over 15 print, length check
    print("It's a long word!") # Print if over 15 length
else: # Do if if and elif are false above
    print("Just right!") # Print if other statements fail

for x in range(5): # For loop that counts from 0 to 5
    print(x) # print the value x from the for loop above

for x in range(2,5): # For loop with start 2, end at 5 (but not printed out)
    print(x) # Print x from for for loop above

for x in range(2,10,3): # For loop: start 2, end 10, increment by 3
    print(x) # Print x from loop above

x = 0 # initialzie x with value 0
while(x < 5): # While loop: while x is less than 5
    print(x) # Print x from loop above
    x += 1 # Increment x for the loop above so it eventually ends

pizza_toppings.pop() # Delete and make use oflast item in list
pizza_toppings.pop(1) # Delete and make use of item at index 1

print(person) # Print dictionary person
person.pop('eye_color') # Remove and make use of key and value in person
print(person) # Print dictionary person

for topping in pizza_toppings: # for item in list pizza_toppings
    if topping == 'Pepperoni': # if item is pepperoni, skip to next item
        continue # continue the loop to next item
    print('After 1st if statement') # Print
    if topping == 'Olives': # If item is Olives stop the loop
        break # Break/stop the loop

def print_hello_ten_times(): # Define function print_hello_ten_times
    for num in range(10): # Loop to run from 0 to 10
        print('Hello') # Print 'Hello'

print_hello_ten_times() # run the function

def print_hello_x_times(x): # Define function with x parameter
    for num in range(x): # Loop for x (argument is the value passed in) number of times
        print('Hello') # Print 'Hello'

print_hello_x_times(4) # Run function and pass argument value

def print_hello_x_or_ten_times(x = 10): # Define function with default parameter
    for num in range(x): # argument is in or default x which is equal to 10
        print('Hello') # Print 'Hello' 10 times, unless different value passed

print_hello_x_or_ten_times() # Run function with default parameter value
print_hello_x_or_ten_times(4) # Run function with argument = 4

"""None of the functions return a value... they do but it's not saved"""

# multilinen commet next 3 lines:
"""
Bonus section
"""

# single line comments below (and this one):

# print(num3) -- This value is not defined; produces error
# num3 = 72 -- Defined after the print; does nothing
# fruit[0] = 'cranberry' -- Can not change a value in a tuple
# print(person['favorite_team']) -- There is no key 'favorite team'
# print(pizza_toppings[7]) -- There is no index 7: out of range
#   print(boolean) -- bad formatting: error produced
"""
The lines below refer to the Tuple. A tuple can not be altered.
You can not add or delete from the tuple
"""
# fruit.append('raspberry')
# fruit.pop(1)
