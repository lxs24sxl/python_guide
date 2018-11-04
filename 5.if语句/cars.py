cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.lower())

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

age = 21 or 11
print(age)

request_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in request_toppings)
print('lxs' in request_toppings)