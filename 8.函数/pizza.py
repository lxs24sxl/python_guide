# def make_pizza(*toppings):
#   print('\nMaking a pizza with the following toppings:')
#   for topping in toppings:
#     print("- " + topping)


# make_pizza('lxs')
# make_pizza('lll', 'xxx', 'sss')

def make_pizza(size, *toppings):
  print('\nMaking a '+str(size)+'-inch pizza with the following toppings:')
  for topping in toppings:
    print("- " + topping)


make_pizza(6, 'lxs')
make_pizza(8, 'lll', 'xxx', 'sss')