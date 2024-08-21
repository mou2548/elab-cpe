username = input("Username: ")
password = input("Password: ")
if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
    print("Welcome, admin.")
else:
    print("You are not admin.")
