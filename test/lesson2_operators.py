user_login = "Admin"
user_pass = "Qwerty123456"

login = input("Login: ")
password = input("Password: ")

if (login == user_login) and (password == user_pass):
    print("Верно!")
else:
    print("Проваливай!")