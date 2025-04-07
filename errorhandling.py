# Error Handling Lab 

# Step 1: Ask user for a filename
original = input("Enter the name of the file you want to read: ")

try:
    # Step 2: Try to open and read the file
    
    with open(original, 'r') as file:
        content = file.read()
        print("\n File content:\n")
        print(content)

except FileNotFoundError:
    print(" Error: That file does not exist.")
except PermissionError:
    print(" Error: You don't have permission to read this file.")
except Exception as e:
    print(f" Error: Unexpected error: {e}")
