# Unlike String lists are mutable
List1 = ["Ahmad","Arslan",7,True,12.4,'s'] # No specific datatype
List1[0] = "Kamran" # chnage Ahmad to Kamran on index 0
print(List1[0]) # Ahmad
print(List1[1]) # Arslan
print(List1[2]) # 7
print(List1[3]) # True
print(List1[4]) # 12.4
print(List1[5]) # s
print(List1[0:3]) # list indexing is just like string
print(List1[7])  # error