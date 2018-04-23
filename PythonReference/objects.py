A blueprint for a house design is like a class description. All the houses built from that blueprint are objects of that class. A given house is an instance.

A Dog is a class.
An object is an instance of a specific dog. Your dog. Your neighbor's dog. Different dogs have different attribute values, but they all have the same attributes.
Dogs have attributes, like a name. Attributes are what an instance IS.
Dogs also have methods, like bork. Methods are what an instance can DO


class Dog:							# Class (any) dog, will describe what it is (attribute) and what it can do (method)

    def __init__(self, name, age): 	# Initializer that used to instantiate objects. argument: self, refers to the object itself.
        self.name = name			# Attribute associated with name argument ... what it is
		self.age = age

		
	def bork(self):					# Method ... what it does
		print("ruff!")

		
    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")
	
	def birthday(self):
        self.age +=1
		
	 def setBuddy(self, bff):		# bff is a Dog object, object is reciprocal
        self.bff = bff
        bff.bff = self
		
>>>bailey = Dog("Bailey", 11)		# A specific instance of an object

>>> print(bailey.name)
[Out]: 'Bailey'

>>> print(bailey.name + " is " + str(bailey.age) + " year(s) old.")
[Out]: Bailey is 11 year(s) old.

>>> bailey.brrk()					# Methods can be called using dot notation
[Out]: ruff!

>>> bailey.doginfo()
[Out]: Bailey is 11 year(s) old.

>>> bailey.age = 12 				# Assign a new value to an attribute
		
>>> bailey.birthday()				# Can also call a method to reassign an attribute value
>>> print(ozzy.age)
[Out]: 13

>>> zipper = Dog("Zipper", 6)
bailey.setBuddy(zipper)

>>> print(bailey.buddy.name)
[Out]: Zipper

>>> print(bailey.buddy.age)
[Out]: 6

>>> bailey.buddy.doginfo()
[Out]: Zipper is 6 year(s) old.

'''
References: 
http://www.oodesign.com
https://www.datacamp.com/community/tutorials/python-oop-tutorial
https://docs.python.org/3/tutorial/classes.html
https://www.learnpython.org/en/Classes_and_Objects
'''
