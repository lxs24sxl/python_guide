filename = 'programming.txt'
# with open(filename, 'w') as file_object:
#   file_object.write('I love programming.\n')
#   file_object.write(' test')


with open(filename, 'a') as file_object:
  file_object.write('I also love finding meaning in large datasets.\n')
  file_object.write('test\n')

with open(filename, 'r') as file_object:
  print(file_object.read()) 