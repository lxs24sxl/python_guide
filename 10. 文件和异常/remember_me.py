import json

def get_stored_username(filename):
  """如果存储了用户名，就获取它""" 
  try:
    with open(filename) as f_obj:
      username = json.load(f_obj)
  except FileNotFoundError:
    return None
  else:
    return username

def get_new_username(filename):
  """提示用户输入用户名""" 
  username = input("What is your name? ")
  with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
  return username

def greet_user(filename):
  """问候用户, 并指出其名称""" 
  username = get_stored_username(filename)
  if username:
    print("Welcome back, {0} !".format(username))
  else:
    username = get_new_username(filename)
    print("We'll remember you when you come back, {0} !".format(username))

filename = 'username.json'
greet_user(filename)