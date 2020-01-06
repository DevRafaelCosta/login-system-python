from db import *


def main():
    while True:
        answer = show_options()
        print('-'*50)

        if answer.startswith('c'):
            print('Create')
            user = input('username: ')
            user = user.lower()
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
                        print('The Password does not match')
            else:
                print('The user already exist')

        elif answer.startswith('l'):
            user = input('Username: ')
            password = input('Password: ')
            user = user.lower()
            login(user, password)

        elif answer.startswith('d'):
            user = input('Username: ')
            password = input('Password: ')
            user = user.lower()

            check = login(user, password)
            if check:
                print(f'\nDelete user: {user}?')
                answer = input('Are you sure? (y/n): ')
                if answer.startswith('y'):
                    account = Account(user, None)
                    account.delete()

        elif answer.startswith('u'):
            user = input('Username: ')
            password = input('Password: ')
            user = user.lower()

            check = login(user, password)
            if check:
                account = Account(user, None)
                print('What do you want to update?')
                print('Password, Name or Message')
                answer = input('-> ').lower()

                if answer.startswith('p'):
                    account.update(1)
                elif answer.startswith('n'):
                    account.update(2)
                elif answer.startswith('m'):
                    account.update(3)
                else:
                    print('Invalid Input')

        elif answer.startswith('s'):
            account = Account(None, None)
            account.show()

        elif answer.startswith('e'):
            break

        else:
            print('Invalid Input')
            answer = input('Close the system? (y/n): ').lower()
            if answer.startswith('y'):
                print('\n\n\n\n\n')
                break
        print('-'*50)
        print('\n\n')


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
            print('Wrong Password')
    else:
        print('This username don\'t exist')


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
