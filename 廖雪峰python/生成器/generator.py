L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(g)

for n in g:
  print(n)