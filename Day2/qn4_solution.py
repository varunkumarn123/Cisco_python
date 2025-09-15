names = input("Enter names separated by spaces: ").split()
sorted_names = sorted(names)
names_tuple = tuple(sorted_names)
with open("names_data.txt", "w") as file:
    file.write("Sorted List: " + str(sorted_names) + "\n")
    file.write("Tuple: " + str(names_tuple) + "\n")
with open("names_data.txt", "r") as file:
    content = file.read()

print("\nData read from file:")
print(content)