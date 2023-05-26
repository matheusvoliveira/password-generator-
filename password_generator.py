import random


class Password:
    def __init__(self):
        self.caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[{]}|;:',<.>/?"

    def multiple_character(self):
        list = []
        for x in range(10):
            password = random.choice(self.caracteres)
            list.append(password)
        full_password = ''.join(list)
        return full_password

    def multiple_password(self):
        quantity = int(input('How many passwords would you like: '))
        all_passwords = []
        print('\nPASSWORDS: \n')
        for x in range(quantity):
            all_passwords.append(self.multiple_character())
        for password in all_passwords:
            print(password)


if __name__ == '__main__':
    test = Password()
    print(20*'-')
    print('PASSWORD GENERATOR')
    print(20*'-')
    test.multiple_password()
