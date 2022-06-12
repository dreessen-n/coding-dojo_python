# Parent file for modularizing

local_val = "magical unicorns"

def square(x):
    """Get the square of the argument"""
    return x * x

class User:
    """Model a user"""
    def __init__(self, name):
        """Initial the user"""
        self.name = name

    def say_hello(self):
        return 'Hello'

print(square(5))
user = User('Anna')
print(user.name)
print(user.say_hello())
# To see available namespace variables use statement below
# print(locals())

print(__name__)

if __name__ == '__main__':
    print('The file is being excuted directly')
else:
    print('The file is being executed because it is imported by another file. The file is called: ', __name__)
