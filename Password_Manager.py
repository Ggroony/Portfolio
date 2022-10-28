from cryptography.fernet import Fernet
import sys

''' 
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)'''


def load_key():
    file = open('key.key', "rb")
    key = file.read()
    file.close()
    return key


attempts = 0

while attempts < 3:
    mps = input("Please enter the Master Password > ")
    key = load_key() + mps.encode()
    fer = Fernet(key)
    if mps != "Peanut!":
        attempts = attempts + 1
        print('Your password is incorrect.')
        if attempts >= 3:
            print('You have failed to login 3 times. The application will now close')
            sys.exit()
    if mps == "Peanut!":
        print('You have successfully logged in!')
        break


def view():
    with open('misc.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            appl, user, pasw = data.split('|')
            print('Application:', appl, ', Username:', user, ', Password:',
                  fer.decrypt(pasw.encode()).decode())


def add():
    app = input('Application Name > ')
    user = input('Username > ')
    pasw = input('Password > ')
    with open('misc.txt', 'a') as f:
        f.write(app + '|' + user + '|' + fer.encrypt(pasw.encode()).decode() + '\n')


while True:
    print("Would you like to:")
    print("1. Add a password?")
    print("2. Check your existing passwords?")
    print("3. Quit")
    userChoice = input()

    if userChoice == "1":
        add()
    if userChoice == "2":
        view()
    if userChoice == "3":
        sys.exit()

### Sources: https://www.youtube.com/watch?v=DLn3jOsNRVE&list=PLk0pDAoLCcFBtIKsjKKONg2BBwCCdUUGO&index=3&t=4993s ###
