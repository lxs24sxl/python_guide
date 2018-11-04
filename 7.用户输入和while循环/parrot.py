# message = input("Tell me something, nad I will repeat it back on you: ")

# print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."

# message = ""
# while message != 'quit':
#   message = input(prompt)
#   if message != 'quit':
#     print(message)


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."

# active = True
# while active:
#   message = input(prompt)
#   if message == 'quit':
#     active = False
#   else:
#     print(message)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

while True:
  message = input(prompt)
  if message == 'quit':
    break
  else:
    print(message)