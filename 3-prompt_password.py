def prompt_password():
    while True:
        password = input("Write password: ")
        if len(password) < 8:
            print("The password must be at least 8 characters long")
        else:
            return password

print(prompt_password())
