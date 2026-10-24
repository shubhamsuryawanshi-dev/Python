a = (1, 2, 23, 323, False, 2, "shubham", "shivam")
print(a)

no = a.count(2) # Count repeated numbers in tuple or any datatype
print(no)

i = a.index(2) # Write a index of that number
print(i)

repeated = a * 3 # Repeate a tuple how you want using '*' keyword
print(repeated)

print(2 in a) # You check if an item exists in tule using 'in' keyword

print(len(a)) # Print the lenght of an tuple using 'len()' keyword

sliced = a[1:4] # Tuples support slicing to create a new from a subset of the original
print(sliced)

b, c, d, e, f, g, h, i = a # Tuples can be unpacked into individual variables
print(b, c, d, e, f, g, h, i)
