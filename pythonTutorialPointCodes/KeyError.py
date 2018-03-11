#!/usr/bin/python
#handling key error in dict when the desired key not found
dict={'name':'Balaji','age':30}
print(dict['age'])
#handling with try except
try:
	print(dict['sex'])
except KeyError:
	print("Desired key 'sex' not found")
#getting the dummy value when key not found 
sex = dict.get("sex",None)
print(sex)
#only immutable hashable keys are allowed
#demonstarting an example , attempting to make list as the key
#dict2 = {['name']:'Balaji'}# this line fails as list of string name is not hashable immutable key for dict
#print(dict2)