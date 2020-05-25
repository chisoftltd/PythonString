# Program by ChisoftMedia
# Accessing String Values


channel = "Python Programming Tutorials"
name = "ChisoftMedia"

str1 = channel[0]
firstname = name[0:7]

print(str1)
print(firstname)

print(name + firstname)

print(str1 * 7)

print(name[3])

print("C" in name)

# Special String Operators

print(name + "\r" + firstname)
print(name + firstname[-5:-2])
print(name + "\n" + firstname)

# Formatting a String
print("My first car was %s. I used it for %d years " %("Vauxhall Insignia", 2))


# Multi-line Strings
text = """it is very good for you to learn programming. 
I also think that starting with Python is probably the
easiest way to achieve it. The remember to watch the 
videos"""

print(text)

print(text.capitalize())

print(text.center(20))

print(text.count("it"))