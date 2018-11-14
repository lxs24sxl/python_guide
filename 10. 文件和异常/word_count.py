def count_wrods(filename):
  """计算一个文件大致包含多少个单词"""
  try:
    with open(filename) as file_object:
      contents = file_object.read()
  except FileNotFoundError:
    msg = "Sorry, the file {0} does not exist.".format(filename)
    print(msg)
  # except UnicodeDecodeError:
  #   # with open(filename, 'rb') as file_object:
  #   with open(filename, 'r', encoding='UTF-8') as file_object:
  #     contents = file_object.read()
  #     # 计算文件大致包含多少个单词
  #     print_info(filename, contents)
  else:
    # 计算文件大致包含多少个单词
    print_info(filename, contents)

def print_info(filename, contents):
  """打印信息"""
  words = contents.split()
  num_words = len(words)
  print("The file {0} has about {1} words".format(filename, str(num_words)))


filenames = ['fof.txt', 'text.txt', 'alice.txt']
for filename in filenames:
  count_wrods(filename)