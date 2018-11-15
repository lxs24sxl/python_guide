def get_formatted_name(first, last, middle=''):
  """构造你全部的名字"""
  if middle:
    full_name = "{0} {1} {2}".format(first, middle, last)
  else:
    full_name = "{0} {1}".format(first, last)
  return full_name
