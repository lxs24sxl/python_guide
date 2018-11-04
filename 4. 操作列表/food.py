my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('test')
friend_foods.append('test2')


print('My favorite foods are:')
print(my_foods)

print("My frend's favorite foods are:")
print(friend_foods)

for item in my_foods[:2]:
  print(item.upper())