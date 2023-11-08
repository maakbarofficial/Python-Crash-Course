name = "Muhammad Ali Akbar"

# working with string methods
print(name.upper())
print(name.lower())

# will find strings through index from 0, 1, 2, 3
# will return -1 if nothing has been found
print(name.find("A"))

# replcing existing string
print(name.replace("Muhammad Ali Akbar", "Misbah Ali"))
print(name)

# finding string using in keyword
print("Muhammad" in name)