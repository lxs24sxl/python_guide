filename = "alice.txt"
try:
  with open(filename) as file_object:
    contents = file_object.read()
except FileNotFoundError:
  msg = "Sorry, the file {0} does not exist.".format(filename)
  print(msg)
else:
  # 计算文件大致包含多少个单词
  words = contents.split()
  num_words = len(words)
  print("The file {0} has about {1} words".format(filename, str(num_words)))