# functions basic ii

print(f'\nexercise 1: Countdown\n')

def countdown(num):
    lst = []
    for i in range(num, -1, -1):
        lst.append(i)
    return lst

x = countdown(5)
print(f'Print the countdown list: {x}')

print(f'\nexercise 2: Print and Return\n')

def print_and_return(num1, num2):
    print(f'Print first argument: {num1}')
    return(num2)

x = print_and_return(1, 2)
print(f'Print the return value: {x}')

print(f'\nexercise 3: First Plus Length\n')

def first_plus_length(lst):
    x = lst[0] + len(lst)
    return x

lst = [1, 2, 3, 4, 5]
value = first_plus_length(lst)
print(f'list: {lst}')
print(f'sum of first value and length of list: {value}')

print(f'\nexercise 4: Values Greater than Second\n')

def values_greater_than_second(lst):
    if len(lst) < 2:
        print(f'length of list is less than 2')
        return False
    else:
        x = lst[1]
        lst2 = []
        for value in lst:
            if lst[value] > x:
                lst2.append(value)
    
        print(f'length of new list: {len(lst2)}')
        return lst2


lst = [5, 2, 3, 2, 1, 4]
lst2 = values_greater_than_second(lst)
print(f'Return list: {lst2}\n')

lst3 = [3]
lst4 = values_greater_than_second(lst3)
print(f'Return list: {lst4}\n')

print(f'\nexercise 5: This length, That Value\n')

def length_and_value(size, value):
    lst = []
    for item in range(0, size):
        lst.append(value)
    return lst

x = length_and_value(4, 7)
y = length_and_value(6, 2)
print(x)
print(y)
    

