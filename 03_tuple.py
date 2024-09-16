# A tuple is an immutable data type in python. 
tuple1 = () # empty tuple
tuple2 = (1,) # with single element in a tuple use ,
tuple3 = (1,2,3,4,6) # with more than one element
print(tuple1)
print(tuple2)
print(tuple3)
print(type(tuple1))

tuple4 = (1) # without , with single value
print(type(tuple4)) # it's integer type not tuple

tuple3 = (8,5,4,6,9)
tuple3[0]=10
print(tuple3)