#Operations

#read specific number of characters

file=open("1.txt" , "r")
print(f"10 character {file.read(10)}")

#First lline

print(f"First line {file.readline()}")

#number of lines

print(f"2 lines {file.readline()} , {file.readline()})")


#Read all lines

print(f"ALL , {file.readlines()}")

#Loop throught lines

for i in file:
    print(i)


file.close()