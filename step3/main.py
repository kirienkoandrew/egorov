def check_password_dictionary(x):
    with open('easy_passwords.txt') as file:
        lst = file.readlines()
        print(lst)

check_password_dictionary('asd')
