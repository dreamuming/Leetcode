from __future__ import print_function

names = ["ben", "Sally", "Amy", "george", "Randy", "Alice"]

for index in range(0,len(names)):
	print(names[index], "is found in index", index)
	
for name in names:
	print(name, "is found in index", names.index(name))