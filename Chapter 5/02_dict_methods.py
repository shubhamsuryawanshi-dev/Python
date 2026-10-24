# NOTE: Dictionary is Mutable
d = {} # Empty dictionary
marks = {
    "Shubham": 100,
    "Harry": 56,
    "Rohan": 23
}

# print(marks.items()) # Print all items in Dictionary using 'items()' keyword
# print(marks.keys()) # Print keys of Dictionary using 'Keys()' keyword
# print(marks.values()) # Print Values of Dictionary using 'values()' keyword
# marks.update({"Shubham": 99, "Renuka": 90}) # Update the Dictionary
# marks.clear() # Removes all elements from the dictionary
# marks.copy() # Returns a shallow copy of the dictionary
# print(marks)


print(marks.get("Shubham2")) # Prints None cuz this name key is not exsist in Dictionary
print(marks["Shubham2"]) # Returns an error if key does not exsist in Dictionary
