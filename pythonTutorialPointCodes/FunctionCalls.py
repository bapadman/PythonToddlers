#!/usr/bin/python
#this file we ll be dicussing the various function calls possible with python

#simple function to print the passed value
def function1(arg):
	print("printing passed value ",arg)
	return

#same function called for different argument types
function1("Hello")
function1(1234)

#callbyvalue sample
def callByValueOnList(list2):
	print("Obtained list ",list2)
	list2.append([1,2,3,4])
	print("modified list ",list2)
	return 

list = [5,6,7]
print("Before calling by value ",list)
callByValueOnList(list)#list value is modified here on append
print("After calling by value ",list)

#callbyreference sample
def callByReferenceOnList(list2):
	print("Obtained list ",list2)
	list2 = [1,2,3,4]
	print("modified list ",list2)
	return 

list3 = [5,6,7]
print("Before calling by value ",list3)
callByReferenceOnList(list3)#original list value is not modified here
print("After calling by value ",list3)

#named & default arguments example
def namedArgument(name,age=30):
	print("name : ",name,"age : ",age)
	return

namedArgument(age=27,name='gautham')#order of arguments jumbled retaining the name of the argument
namedArgument(name='balaji')#age not supplied here , will be taking the default

#var arg sample
def varArg(manArg,*args):
	print("Printing manArg ",manArg)
	print("Printing other args ")
	for arg in args:
		print(arg)
	return

varArg("hello")
varArg("hello","this","is","balaji")
