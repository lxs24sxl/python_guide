def build_person(first_name, last_name, age=""):
  person = {'first_name': first_name, "last_name": last_name }
  if age:
    person['age'] = age
  else:
    person['age'] = 21
  return person

print(build_person("lin", "xiaoshun", 22))