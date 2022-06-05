# Hello World assignment - python - python fundamental

# 1. TASK: print "Hello World"
print('Hello World!')

# 2. print "Hello Noelle!" with the name in a variable
name = "Neal"
print('Hello,',name)	# with a comma
print('Hello, ' + name)	# with a +

# 3. print "Hello 42!" with the number in a variable
name = 13
print('Hello,',name)	# with a comma
print('Hello, ' + str(name))	# with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "indian food"
fave_food2 = "ema datsi"
print('I love to eat {} and {}.'.format(fave_food1.title(), fave_food2.title())) # with .format()
print(f'I love to eat {fave_food1.title()} and {fave_food2.title()}.') # with an f string


