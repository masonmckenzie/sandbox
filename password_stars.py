"""
CP1404- Practical 02
Mason McKenzie
Password checker
"""
def get_password():
    i = 0
    while i != 1:
        password = input('make password: ')
        min_length = 4
        if len(password) < min_length:
            print('password length needs to be increased')
        else:
            i = 1
    return password
def print_password():
    password = get_password()
    for i in range(0, len(password)):
        print(end='*')
print_password()
