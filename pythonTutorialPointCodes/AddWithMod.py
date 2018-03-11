#!/usr/bin/python
# modules are looked up in the oreder mentioned below
# The current directory.
# If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH.
# If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.
from MathModule import add
a=10
b=5
c=add(a,b)
print(c)
from MathModule import sub
c=sub(a,b)#above import is necessary
print(c)