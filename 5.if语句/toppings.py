requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']



if requested_toppings:
  for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
      print('Sorry, we are out of green peppers right now.')
    else:
      print('Adding ' + requested_topping + '.')
  print('\nFinshing making your pizza!')
else:
  print('Are you sure you ant a plain pizza!')

avaliable_toppings = ['mushrooms', 'extra cheese']
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']



if requested_toppings:
  for requested_topping in requested_toppings:
    if requested_topping not in avaliable_toppings:
      print('Sorry, we are out of ' + requested_topping +' right now.')
    else:
      print('Adding ' + requested_topping + '.')
  print('\nFinshing making your pizza!')
else:
  print('Are you sure you ant a plain pizza!')