with open("user/password.txt", "r") as password_file:
    password = password_file.read().strip()

with open("user/username.txt", "r") as username_file:
    username = username_file.read().strip()
