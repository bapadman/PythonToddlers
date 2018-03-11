#!/usr/bin/python
#demonstrating the dir sample
import MathModule
from importlib import reload
print(dir(MathModule))
#demonstrating globals n locals sample
str = 'hello'
def sample():
	name = 's'
	print("locals => ",locals()) # prints all elements with in the function , just name s in this case 
	print("globals => ",globals()) # prints all elements outside the function , including imported modules 
	#return type of both the above methods are dictionaries
	return
sample()

# reloading modules 
reload(MathModule) # math module loaded twice , you ll see the print line printed again

