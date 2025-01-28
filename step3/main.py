def check_password_dictionary(x):
    with open('easy_passwords.txt') as file:
        lst = file.read()
        return x in lst


