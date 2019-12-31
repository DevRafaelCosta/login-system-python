from db import *


def main():
    while True:
        print('-'*20)
        print('  LOGIN SYSTEM  ')
        print('-'*20)
        print('Login - ("l")')
        print('Create - ("c")')
        print('Delete - ("d")')
        print('Update - ("u")')
        print('Show Users - ("s")')
        print('Exit - ("e")')
        answer = input('-> ').lower()
        print()


        if answer.startswith('l'):
            user = input('Username: ')
            account = Account(user, None)
            user_check = account.user_check()

            if user_check:
                password = input('Password: ')
                account = Account(user, password)
                pass_check = account.pw_check()
                if pass_check:
                    account.login()
                else:
                    print('Wrong Password\n')
            else:
                print('This username don\'t exist\n')


        elif answer.startswith('c'):
            pass


        elif answer.startswith('d'):
            pass


        elif answer.startswith('u'):
            pass


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


if __name__ == '__main__':
    main()
