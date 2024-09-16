tuple1 = (1,2,3,"Berlin","Madrid","New York", 4,5,6,7,1)
tuple2 = (9,8,76,5)
print(tuple1.count(1)) # return the number of occurance of 1
print(tuple1.index("Berlin")) # return Index of Berlin
print(tuple1[5])
print(tuple1[1:6]) # slicing
tuple3 = tuple1 + tuple2   # concatenate two tuples
print(tuple3)
print(tuple2 * 3)   # tuple repeat 3 times by using * symbol
print(8 in tuple2)   # check the existance of item in a tuple by using keyword "in"
print(len(tuple3))   # return number of item

tuple4 = (1,2,3)
a,b,c = tuple4    # You can unpack tuple elements into individual variables.
print(a)
print(b)
print(c)


