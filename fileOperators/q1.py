user_input = input("Enter your text: ")

# Write to file
file_name = "q1.txt"
with open(file_name, "w") as file:
    file.write(user_input)

# Read from file
with open(file_name, "r") as file:
    file_content = file.read()

# Display file content
print("File Content:")
print(file_content)
