file=open("Codingal (1).txt" , "r")
print(file.read(20))
file.close()

file=open("Codingal (1).txt" , "a")
file.write("Hello , How are you")
file.close()