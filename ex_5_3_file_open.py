file = open("basic.txt", "w")
print(type(file)) # <class '_io.TextIOWrapper'> 

file.write("Hello Python Programmin...!")

file.close()