from array import *
values = array('b',[5,3,6,2,5])
for b in range(len(values)):
    # an array for printing the values in the given index
    print(values[b])
newArr = array(values.typecode, (a*a for a in values))
for e in newArr:
    print(e)