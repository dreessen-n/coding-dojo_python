# Core assignment - For Loop Basic 1

# Basic - print all integers from 0 to 150
for i in range(0, 151):
    print(i)

# Multiples of 5 - print all multiples of 5 from 5 to 1000
for i in range(5, 1001, 5):
    print(i)

# Counting, the Dojo Way - print integers 1 to 100. if divisible by 5,
# print 'Coding' if divisible by 10, print 'Coding Dojo'
for i in range(1, 101):
    if ((i % 10) == 0):
        print('Coding Dojo')
    elif ((i % 5) == 0):
        print('Coding')
    else:
        print(i)

# Whoa. That Sucker's Huge - add odd numbers from 0 to 500_000_000 and 
# Print final sum
sum = 0
for i in range(1, 500_001, 2):
    sum = sum + i

print(sum)

# Countdown by fours - print positive numbers starting at 2018, counting
# down by fours
for i in range(2018, 0, -4):
    print(i)

"""
Flexible counter - Set 3 variables: lowNum, highNum, mult. Starting at
lowNum and going through highNum, print only the integers that are a 
multiple of mult. For example, if lowNum = 2, highNum = 9, and mult = 3,
the loop should print 3, 6, 9 (on successive lines)
"""
low_num = 3
high_num = 9
mult = 3
for i in range(low_num, high_num + 1):
    if (i % mult) == 0:
        print(i)

