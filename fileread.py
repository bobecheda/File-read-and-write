# File Read & Write Challenge 

# Step 1: Open and read from the original file
with open(r'C:\Users\user\Desktop\PYTHON SESSIONS\WEEK 4\original.txt', 'r') as infile:
    content = infile.read()

# Step 2: Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Step 3: Write the modified content to a new file
with open('modified.txt', 'w') as outfile:
    outfile.write(modified_content)

print("Original File has been read and modified content written to 'modified.txt'")
