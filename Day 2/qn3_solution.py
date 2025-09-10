sentence = input("Enter a sentence: ")
words_list = sentence.split()
words_tuple = tuple(word.upper() for word in words_list)
file_name = 'sentence_data.txt'
with open(file_name, 'w') as file:
    file.write(f"List: {words_list}\n")
    file.write(f"Tuple: {words_tuple}\n")


with open(file_name, 'r') as file:
    list_line = file.readline().strip()
    tuple_line = file.readline().strip()

print(list_line)
print(tuple_line)
