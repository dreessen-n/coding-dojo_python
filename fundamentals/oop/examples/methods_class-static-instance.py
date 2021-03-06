"""
This is an example for @classmethod and @staticmethod 
from website Real Python
"""

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

"""
Instance Methods
The first method on MyClass, called method, is a regular instance method. That’s the basic, no-frills method type you’ll use most of the time. You can see the method takes one parameter, self, which points to an instance of MyClass when the method is called (but of course instance methods can accept more than just one parameter).

Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.

Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state.
"""

"""
Class Methods
Let’s compare that to the second method, MyClass.classmethod. I marked this method with a @classmethod decorator to flag it as a class method.

Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.

Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.
"""

"""
Static Methods
The third method, MyClass.staticmethod was marked with a @staticmethod decorator to flag it as a static method.

This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).

Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.
"""

print("call an instance method:")
obj = MyClass()
obj.method()
print(obj.method())
print()

"""
print shows 'instance method called' - which confirms access to object method
This confirmed that method (the instance method) has access to the object instance (printed as <MyClass instance>) via the self argument.
"""

"""
When the method is called, Python replaces the self argument with the instance object, obj. We could ignore the syntactic sugar of the dot-call syntax (obj.method()) and pass the instance object manually to get the same result:
"""
print("another version of instance method")
MyClass.method(obj)
print(MyClass.method(obj))
print()

"""
By the way, instance methods can also access the class itself through the self.__class__ attribute. This makes instance methods powerful in terms of access restrictions - they can modify state on the object instance and on the class itself.
"""

"""
Let's try out the class method next:
"""
print("call classmethod:")
obj.classmethod()
print(obj.classmethod())
print()

"""
Calling classmethod() showed us it doesn’t have access to the <MyClass instance> object, but only to the <class MyClass> object, representing the class itself (everything in Python is an object, even classes themselves).

Notice how Python automatically passes the class as the first argument to the function when we call MyClass.classmethod(). Calling a method in Python through the dot syntax triggers this behavior. The self parameter on instance methods works the same way.

Please note that naming these parameters self and cls is just a convention. You could just as easily name them the_object and the_class and get the same result. All that matters is that they’re positioned first in the parameter list for the method.

Time to call the static method now:
"""
print("call staticmethod:")
obj.staticmethod()
print(obj.staticmethod())
print()

"""
Did you see how we called staticmethod() on the object and were able to do so successfully? Some developers are surprised when they learn that it’s possible to call a static method on an object instance.

Behind the scenes Python simply enforces the access restrictions by not passing in the self or the cls argument when a static method gets called using the dot syntax.

This confirms that static methods can neither access the object instance state nor the class state. They work like regular functions but belong to the class’s (and every instance’s) namespace.

Now, let’s take a look at what happens when we attempt to call these methods on the class itself - without creating an object instance beforehand:
"""

print("call classmethod with out obj:")
MyClass.classmethod()
print(MyClass.classmethod())
print()

print("call staticmethod with out obj:")
MyClass.staticmethod()
print(MyClass.staticmethod())
print()

print("call instance method() with out obj:")
# MyClass.mehtod()
# print(MyClass.method())
print()

"""
method call produces error:
TypeError: unbound mehtod method() must be called with MyClass instance as 
first argument (go nothing instead)
"""

"""
We were able to call classmethod() and staticmethod() just fine, but attempting to call the instance method method() failed with a TypeError.

And this is to be expected — this time we didn’t create an object instance and tried calling an instance function directly on the class blueprint itself. This means there is no way for Python to populate the self argument and therefore the call fails.

This should make the distinction between these three method types a little more clear. But I’m not going to leave it at that. In the next two sections I’ll go over two slightly more realistic examples for when to use these special method types.

I will base my examples around this bare-bones Pizza class:
"""

"""
The Italians figured out their pizza taxonomy centuries ago, and so these delicious types of pizzas all have their own names. We’d do well to take advantage of that and give the users of our Pizza class a better interface for creating the pizza objects they crave.

A nice and clean way to do that is by using class methods as factory functions for the different kinds of pizzas we can create:
"""

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutoo(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

"""
Note how I’m using the cls argument in the margherita and prosciutto factory methods instead of calling the Pizza constructor directly.

This is a trick you can use to follow the Don’t Repeat Yourself (DRY) principle. If we decide to rename this class at some point we won’t have to remember updating the constructor name in all of the classmethod factory functions.

Now, what can we do with these factory methods? Let’s try them out:
"""

print(Pizza.margherita())

print(Pizza.prosciutoo())

"""
As you can see, we can use the factory functions to create new Pizza objects that are configured the way we want them. They all use the same __init__ constructor internally and simply provide a shortcut for remembering all of the various ingredients.

Another way to look at this use of class methods is that they allow you to define alternative constructors for your classes.

Python only allows one __init__ method per class. Using class methods it’s possible to add as many alternative constructors as necessary. This can make the interface for your classes self-documenting (to a certain degree) and simplify their usage.
"""

"""
When To Use Static Methods
It’s a little more difficult to come up with a good example here. But tell you what, I’ll just keep stretching the pizza analogy thinner and thinner… (yum!)

Here’s what I came up with:
"""

import math

class PizzaStatic:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'PizzaStatic({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

"""
Now what did I change here? First, I modified the constructor and __repr__ to accept an extra radius argument.

I also added an area() instance method that calculates and returns the pizza’s area (this would also be a good candidate for an @property — but hey, this is just a toy example).

Instead of calculating the area directly within area(), using the well-known circle area formula, I factored that out to a separate circle_area() static method.
"""

p = PizzaStatic(4, ['mozzarella', 'tomatoes'])
print(p)
p.area()
print(p.area())
PizzaStatic.circle_area(4)
print(PizzaStatic.circle_area(4))

"""
Sure, this is a bit of a simplistic example, but it’ll do alright helping explain some of the benefits that static methods provide.

As we’ve learned, static methods can’t access class or instance state because they don’t take a cls or self argument. That’s a big limitation — but it’s also a great signal to show that a particular method is independent from everything else around it.

In the above example, it’s clear that circle_area() can’t modify the class or the class instance in any way. (Sure, you could always work around that with a global variable but that’s not the point here.)

Now, why is that useful?

Flagging a method as a static method is not just a hint that a method won’t modify class or instance state — this restriction is also enforced by the Python runtime.

Techniques like that allow you to communicate clearly about parts of your class architecture so that new development work is naturally guided to happen within these set boundaries. Of course, it would be easy enough to defy these restrictions. But in practice they often help avoid accidental modifications going against the original design.

Put differently, using static methods and class methods are ways to communicate developer intent while enforcing that intent enough to avoid most slip of the mind mistakes and bugs that would break the design.

Applied sparingly and when it makes sense, writing some of your methods that way can provide maintenance benefits and make it less likely that other developers use your classes incorrectly.

Static methods also have benefits when it comes to writing test code.

Because the circle_area() method is completely independent from the rest of the class it’s much easier to test.

We don’t have to worry about setting up a complete class instance before we can test the method in a unit test. We can just fire away like we would testing a regular function. Again, this makes future maintenance easier.
"""

"""
Key Takeaways
Instance methods need a class instance and can access the instance through self.
Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.
"""


