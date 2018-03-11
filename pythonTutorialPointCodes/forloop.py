#!/usr/bin/python
from array import array
#demonstrating for loop
#for in range 
for i in range(3):
	print(i)
#for to find prime numbers between 10 and 20
for i in range(10,20):
	iIsPrime = True
	for j in range(2,i-1):
		if(i%j == 0):
			#print(i," is divisible by ",j)
			#print("Continuing in next element")
			iIsPrime = False
			break
	if iIsPrime:
		print(i," is prime ")
# using for loop on collections - arrays , tuples , list , dictionaries
# for on string
print("for each on string")
for char in 'Balaji':
	print(char)
# for on array / list
# diff betn array n list ? how to create array / list is quite ambiguous 
print("for each on list")
arr = [1,"two",3,4,5,4]
arr.append(6)
for a in arr:
	print(a)
#for on tuples
#list n tuple are same except , they are immutable . 
#you cannot delete / insert an index belonging to particular index
print("for each on tuples")
tup = (1,"3",3,7,5,4)
#tup.append(6) #uncommenting this line gives error
for t in tup:
	print(t)
#for on set
print("for each on set")
st = set([1,"two",3,4,5,4])
for s in st:
	print(s*2)
#for on dictionaries
#dictionaries resemble regular json format
print("for each on dictionary")
dc = {'name':'Balaji','age':30}
for key in dc:
	print(key," -> ",dc[key])
# new style in python 3
print("printing from new items method in py3")
for key,value in dc.items():
	print(key,"->",value)

