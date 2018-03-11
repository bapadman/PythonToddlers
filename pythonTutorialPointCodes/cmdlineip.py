#!/usr/bin/python
#raw_input -> getting txt input from console
#raw_input has been transformed to input in python 3
s = input("Enter any raw input")
print("The input u entered is ",s)
try:
	print("Evaluating the expression passed ",eval(s))
except NameError: # try catch with name error
	print("Not a valid expression for evaluation ...")
except SyntaxError:
	print("please check the expression syntax")

# sample output with expression

#Balajis-MacBook-Air:tutorialpointCodes bala$ python cmdlineip.py 
#Enter any raw input[x*5 for x in range(2,10,2)]
#The input u entered is  [x*5 for x in range(2,10,2)]
#Evaluating the expression passed  [10, 20, 30, 40]