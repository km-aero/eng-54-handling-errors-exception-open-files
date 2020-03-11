# opening files using 'with'

try:
    file = open('order.txt', 'r')

except FileNotFoundError as err:
    print('Check your files')
    print(err)
    raise # raises an exception