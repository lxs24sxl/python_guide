def get_formatted_name(first_name, last_name):
  """返回整洁的名称"""
  full_name = first_name + " " + last_name
  return full_name.title()

man = get_formatted_name("bryant", 'kobe')
print(man)