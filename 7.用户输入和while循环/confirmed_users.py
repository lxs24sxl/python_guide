unconfirmed_users = ['alice', 'brian', 'candace']
confirm_users = []

while unconfirmed_users:
  current_user = unconfirmed_users.pop()
  print('Verifying user: ' + current_user.title())
  confirm_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirm_user in confirm_users:
  print(confirm_user)