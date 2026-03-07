# 1) Take two file names from the user:
#    a) First file → the file where content will be added.
first_file=input("Enter the name of the first file")
second_file=input("Enter the name of the second file")
#    b) Second file → the file whose content will be copied.

# 2) Open both files in read mode:
f1=open(first_file , "r")
f2=open(second_file , "r")

#    a) Read and print the content of the first file.
print(f"Content of first file before appending : \n {f1.read()}" )
print(f"Content of second file before appending : \n {f2.read()}")

#    b) Read and print the content of the second file.
#    c) Close both files.
f1.close()
f2.close()

# 3) Open the first file in append mode and the second file in read mode:

f1=open(first_file , "a")
f2=open(second_file , "r")

#    a) Read the second file’s content.
#    b) Write (append) it into the first file.
f1.write(f2.read())

# 4) Move the cursor back to the beginning using `seek(0)`:

f1.seek(0)
f2.seek(0)
#    a) This helps to read the full updated content from the start.

# 5) Print the content of both files after appending.

print(f"Content of both files after appending: \n {f1.read()}")
print(f"Content of both files after appending : \n {f2.read()}")

# 6) Close both files to save and finish.
f1.close()
f2.close()