from db import *


def main():
    while True:
        answer = show_options()

        if answer.startswith('c'):
            print('\nCreate')
            user = input('username: ')
            account = Account(user, None)
            user_check = account.user_check()

            if not user_check:
                while True:
                    password = input('Create a Password: ')
                    check = input('Confirm your Password: ')
                    if password == check:
                        account = Account(user, password)
                        account.create()
                        break
                    else:
                        print('The Password does not match\n')
            else:
                print('The user already exist\n')

        elif answer.startswith('l'):
            user = input('Username: ')
            password = input('Password: ')
            login(user, password)

        elif answer.startswith('d'):
            user = input('Username: ')
            password = input('Password: ')

            check = login(user, password)
            if check:
                print(f'Delete user: {user}?')
                answer = input('Are you sure? (y/n): ')
                if answer.startswith('y'):
                    account = Account(user, None)
                    account.delete()
            print()

        elif answer.startswith('u'):
            pass
            """
            check = login()
            print('What do you want to update?')
            print('Password, Name or Message')
            answer = ('-> ').lower()
            """

        elif answer.startswith('s'):
            pass

        elif answer.startswith('e'):
            break

        else:
            print('Invalid Input')
            answer = input('Close the system? (y/n): ').lower()
            print()
            if answer.startswith('y'):
                break


def login(user, password):
    account = Account(user, None)
    user_check = account.user_check()

    if user_check:
        account = Account(user, password)
        pass_check = account.pw_check()
        if pass_check:
            account.login()
            return True
        else:
            print('Wrong Password\n')
    else:
        print('This username don\'t exist\n')


def show_options():
    print('-'*20)
    print('  LOGIN SYSTEM  ')
    print('-'*20)
    print('Create - ("c")')
    print('Login - ("l")')
    print('Delete User - ("d")')
    print('Update - ("u")')
    print('Show Users - ("s")')
    print('Exit - ("e")')
    answer = input('-> ').lower()
    print()
    return answer


if __name__ == '__main__':
    main()
