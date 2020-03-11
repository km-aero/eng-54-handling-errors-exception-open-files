# use open to open a file
# file = open('order.txt')

try:
    file = open('order.txt', 'r') # you should close after you open a file
    file_line_list = file.readlines()
except FileNotFoundError as errmsg:
    print('Please check the file exists.')
    print(errmsg) # prints the actual error

print(file_line_list)

[print(line.rstrip('\n')) for line in file_line_list]

file.close() # closes file