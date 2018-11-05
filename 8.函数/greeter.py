# def greet_user(username,age = 21):
#   """显示简单的问候语"""
#   print("Hello!" + username.title() + ", is your age " + str(age) +"?")
# greet_user('linxiaoshun', 21)

# greet_user(age=21, username="lxs")

# greet_user(username="lxs2")

def get_formatted_name(first_name, last_name):
  full_name = first_name + " " + last_name
  return full_name

while True:
  print('\nPlease tell me your name:')
  print("(enter 'q' at any time to quit)")

  f_name = input("First name: ")
  if f_name == 'q':
    break
  l_name = input("Last name: ")
  if l_name == 'q':
    break

  formatted_name = get_formatted_name(f_name, l_name)
  print("\nHello, " + formatted_name + "!")

 