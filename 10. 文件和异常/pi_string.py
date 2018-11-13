import file_reader

pi_string = ''
for line in file_reader.lines:
  pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
  print('yes')
else:
  print('shit')