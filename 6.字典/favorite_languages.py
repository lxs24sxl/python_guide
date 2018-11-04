fl = {
  'jen': 'js',
  'sarah': 'java',
  'lxs': 'python',
  'zal': 'python',
}

for name, language in fl.items():
  print(name.title() +" 's favorite language is " + language.title() )

for name in fl.keys():
  print(name.title())

friends = ['sarah', 'lxs']
for name in fl.keys():
  if name in friends:
    print(" Hi " + name.title() + 
        ", I see your favorite language is " + 
        fl[name].title() + "!")

if 'zal' not in fl.keys():
  print('zal, please take our poll!!!')

for language in set(fl.values()):
  print(language.title())


fl2 = {
  'jen': ['python', 'ruby'],
  'sarah': ['python', 'javascript'],
  'lxs': ['python', 'javascript', 'java']
}

same = []
for name, languages in fl2.items():
  print("\n" + name.title() + "'s favorite languages are:")
  for language in languages:
    if 'javascript' in language:
      same.append(name)
    print("\t" + language.title())

print('javscript', same)
