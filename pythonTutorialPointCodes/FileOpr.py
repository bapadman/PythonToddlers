#!/usr/bin/python
#file operations sample
#creating and writing file
fo = open("Months","wb")#you are writing to a file in binary mode 
fo.write("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".encode('utf-8'))#convert string to byte and write 
fo.close

fo = open("Months","rb")
chr = fo.read(1).decode('utf-8')
while chr != "":
	print(chr)
	chr = fo.read(1).decode('utf-8')