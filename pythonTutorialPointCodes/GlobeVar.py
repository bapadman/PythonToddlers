#!/usr/bin/bash
#global n local var illustration
total = 10
def sum(a1,a2):
	total = a1+a2 # this total var is assumed to be declared here
	return total
print("global total ",total)# please notice global total value unaltered here
print("local total ",sum(10,20))

# manipulating global sum
def sumGlobal(a1,a2):
	global total 
	total = a1+a2
	return
sumGlobal(10,20)
print("Printing global total agian ",total)
