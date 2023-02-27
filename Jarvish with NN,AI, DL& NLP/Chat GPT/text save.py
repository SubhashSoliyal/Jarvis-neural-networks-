# Open file in append mode
file = open("file.txt", "a")

# Add new text to the file
file.write("This is new text.\n")

# Read the contents of the file
# with open("file.txt", "r") as file:
#     old_text = file.read()

old_text = "hello\n"
# Append the old text to the file
file.write(old_text)

# Close the file
file.close()

# Open the file again in read mode and print the contents
with open("file.txt", "r") as file:
    print(file.read())

