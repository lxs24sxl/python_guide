squares = []
for value in range(1, 11):
  square = value**2
  squares.append(square)
print('前10个整数的平方', squares)


print(min(squares))
print(max(squares))
print(sum(squares))


suqares = [value**2 for value in range(1, 11)]
print(squares)