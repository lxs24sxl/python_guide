# with open('./pi_digits.txt') as file_object:
#   content = file_object.read()
#   print(content.rstrip())



# with open('./pi_digits.txt') as file_object:
#   for line in file_object:
#     print(line.rstrip())



with open('./pi_digits.txt') as file_object:
  lines = file_object.readlines()

# for line in lines:
#   print(line.rstrip())