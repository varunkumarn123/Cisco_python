numbers_str = input("Numbers (space seperated):")
numbers_list = [int(num_str) for num_str in numbers_str.split()]
print(numbers_list)
num_sum = sum(numbers_list)
num_avg = num_sum / len(numbers_list)
print(num_sum)
print(num_avg)


file_name = 'number_data.txt'
with open(file_name, 'w') as writer:
    writer.write(f'List: {numbers_list}\n')
    writer.write(f'Sum: {num_sum}\n')
    writer.write(f'Average: {num_avg}')

with open(file_name,'r') as reader:
    line_list = reader.readline()
    line_sum = reader.readline()
    line_avg = reader.readline()
    print(line_list)
    print(line_sum)
    print(line_avg)