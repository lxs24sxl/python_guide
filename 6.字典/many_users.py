users = {
  "lxs": {
    "first": "albert",
    "last": "einstein",
    "location": "princeton",
  },
  "zal": {
    "first": "marie",
    "last": "curie",
    "location": "paris",
  },
}

for username, user_info in users.items():
  print("\nUsername:" + username.title())
  full_name = user_info['first'] + " " + user_info["last"]
  location = user_info['location']

  print("\tFull name:" + full_name.title())
  print("\tLocation:" + location.title())