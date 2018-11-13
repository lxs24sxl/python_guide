from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'Python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'


favorite_languages2 = OrderedDict()

favorite_languages2['sarah'] = 'c'
favorite_languages2['jen'] = 'Python'
favorite_languages2['edward'] = 'ruby'
favorite_languages2['phil'] = 'python'

for name, language in favorite_languages.items():
  print(name.title() + " 's favorite language is " + language.title() + ".")

print(favorite_languages==favorite_languages2)

print("Regular dictionary")
d1={}
d1['a']='A'
d1['b']='B'
d1['d']='d'
d1['c']='C'

d2={}
d2['b']='B'
d2['a']='A'
d2['d']='d'
d2['c']='C'

print(d1==d2)

from random import randint 
x = randint(1, 6)
print('x: ' + str(x) )