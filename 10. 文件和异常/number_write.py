import json
numbers = {}
numbers['number'] = [1, 2, 4, 6, 7, 11]
numbers['name'] = 'lxs'
filename = 'number.json'
with open(filename, 'w') as f_obj:
  json.dump(numbers, f_obj)