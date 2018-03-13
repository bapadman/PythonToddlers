#!/usr/bin/python
#Trying to understand exception handling structure in python

try:
	fh = open("sample.txt","r")
	#fh = open("forloop.py","r")
except Exception as e:
	print("Exception occured ",str(e))
#except block can take any of the forms below
#except:
#except IOError:
#except IOError,FileError:
else:
	print("operation success")
###finally: # tried finally still not clear with syntx need to try it out
	fh.close()
	print("File closed properly")
