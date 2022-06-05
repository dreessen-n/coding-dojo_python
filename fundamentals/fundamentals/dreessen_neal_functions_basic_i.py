#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
"""My prediction: prints 5"""

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
"""My prediction: error: function not defined"""

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
"""My prediction: will print 5 or error: for double return in func"""

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
"""
My prediction: returns 5 and prints 5 once. Print in func never happens
function ends as soon as return is hit
"""

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
"""
My prediction: print 5 twice; once in func and once outside
It only printed once in side function, it didn't actual save with out 
return statement so prints none
"""

#6
def add(b,c):
    print(b+c)
    # return (b+c)
print(add(1,2) + add(2,3))
"""
My prediction: will print: 3, 5, 8
Solution: printed 3, 5 then thru an error: type error can't add because 
nothing is returned. Need return statement to run
"""

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
"""My prediction: prints 25: you have return statement and cat strings"""

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
"""My prediction: prints: 100, 10"""

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
"""My prediction: prints 7, 14, 21"""

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
"""My prediction: prints 8"""

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
"""
My precdiction: I'm not sure on this one... I think there isn't scope in
python like js and it changes the b value to 300 in func and outside too
so printed will be: 500, 500, 300, 300 (or 500 depending on scope)
Solution: scope does work so global b not changed so output is:
500, 500, 300, 500
"""

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
"""My prediction: same output as #11: 500, 500, 300, 500.
It has a return to change b value but is never saved so value not changed
"""

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
"""My prediction: prints 500, 500, 300, 300. Return is saved this time"""

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
"""My prediction: prints 1, 3, 2"""

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
"""My prediction: prints 1, 3, 5, 10"""
