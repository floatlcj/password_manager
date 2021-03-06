import re
import random
import string
import sys
import os
def imcolorama():
    """
    This function will check if the computer has installed colorama.
    If not, it will install itself, work on both Mac and Windows.
    """
    try:
        import colorama
    except ImportError:
        if os.name == "posix":
            os.system("python3 -m pip install colorama")
        elif os.name == "nt":
            os.system("python -m pip install colorama")


imcolorama()


from colorama import Fore


def impyperclip():
    """
    This function will check if the computer has installed pyperclip.
    If not, it will install itself, work on both Mac and Windows.
    """
    try:
        import pyperclip
    except ImportError:
        if os.name == 'posix':
            os.system('python3 -m pip install pyperclip')
        elif os.name == 'nt':
            os.system('python -m pip install pyperclip')


impyperclip()


import pyperclip


def encry(p,k):
    """"
    This function encrypt a character or symbol based
    on the given key.
    """
    p = ord(p)
    k = ord(k)
    c = (p + k - 32*2) % 95 + 32
    return chr(c)

def decry(c,k):
    """
    This function decrypt the cypher character based
    on the given key.
    """
    c = ord(c)
    k = ord(k)
    p = (c-k) % 95 + 32
    return chr(p)


def encryF(pa,key):
    """"
    This function encrypt the password based on given
    keys.
    """
    times = (len(pa)//len(key)) + 1
    keys = key * times
    cp = ''
    i = 0
    for p in pa:
        cp += encry(p,keys[i])
        i += 1
    return cp

    
def decryF(cp,key):
    """
    This function decrypt the cypher password based
    on the given keys.
    """

    times = (len(cp)//len(key)) + 1
    keys = key * times
    pa = ''
    i = 0
    for p in cp:
        pa += decry(p,keys[i])
        i += 1
    return pa


def read_file_list(filename):
    """
    This function read the password file and returns
    a list of items.
    """
    with open(filename,'a') as infile:
        infile.close()
    with open(filename,'r') as refile:
        templ = refile.readlines()
        newlist = []
        for x in templ:
            nx = x.removesuffix('\n')
            newlist.append(nx)
        refile.close()
    return newlist


def store_password(name,password,key):
    """
    This function can store the password in the
    text file.
    name = name of the password
    password = password to store
    key = key to encrypt the password
    It can also check if the name of the password
    already exists. If yes, it will tell you to use
    "Password Update" function.
    """
    names = read_file_list('names.txt')
    if name not in names:
        with open('names.txt','a') as inna:
            inna.write(name)
            inna.write('\n')
            inna.close()
        with open('password.txt','a') as inpa:
            npass = encryF(password,key)
            inpa.write(npass)
            inpa.write('\n')
            inpa.close()
        return print(Fore.LIGHTBLUE_EX + 'Password stored.'),password_stren(password)
    else:
        return 'The name already exists. Please use Update Password function.'


def retrieve_password(name,key):
    """
    This function is used to retrieve password.
    name = name of the password
    key = the key you used to encrypt the password
    If you don't have the key, you can't get the
    correct password.
    """
    names = read_file_list('names.txt')
    passwords = read_file_list('password.txt')
    if name in names:
        i = names.index(name)
        password = decryF(passwords[i],key)
        return password
    else:
        return 'This name does not exist.'


def update_password(name,oldpass,newpass,oldkey,newkey):
    """
    This function can update the password.
    You need to have the old password and the old key.
    """
    names = read_file_list('names.txt')
    passwords = read_file_list('password.txt')
    if name in names:
        i = names.index(name)
        password = decryF(passwords[i],oldkey)
        if password == oldpass:
            passwords[i] = encryF(newpass,newkey)
            with open('password.txt','w') as inpa:
                for p in passwords:
                    inpa.write(p)
                    inpa.write('\n')
                inpa.close()
            return 'The update is successful.'
        else:
            return 'The old password or old key is incorrect.'
    else:
        return 'The name does not exist.'


def password_stren(password):
    """
    This function check the strength of a password.
    Strong, medium, and weak.
    """

    l = False
    d = False
    low = False
    up = False
    sym = False
    lb = Fore.LIGHTBLUE_EX
    lc = Fore.LIGHTCYAN_EX
    if len(password) >= 8:
        l = True
    if re.search(r'\d',password):
        d = True
    if re.search(r'[a-z]',password):
        low = True
    if re.search(r'[A-Z]',password):
        up = True
    if re.search(r'[!@#$%^&*()_+=|?/.,]',password):
        sym = True
    if l == True and d == True and low == True and up == True and sym == True:
        return print(lb + 'The password strength is' + lc + ' strong.')
    elif l == d == low == up == True:
        return print(lb + 'The password strength is' + lc + ' medium.')
    elif l == d == low == True:
        return print(lb + 'The password strength is' + lc + ' medium.')
    elif l == d == True:
        return print(lb + 'The password strength is' + lc + ' weak.')
    else:
        return print(lb + 'The password strength is' + lc + ' weak.')


def password_generator():
    """
    It randomly generates a password with strong strength.
    """
    random_password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)for i in range(16))
    return random_password


def main():
    """
    The main function. Program interface.
    """
    print('\n\n')
    print(Fore.LIGHTMAGENTA_EX + '1. Store password.')
    print('2. Retrieve password.')
    print('3. Update password.')
    print('4. Check password strength.')
    print('5. Password Generator')
    print('6. Exit.')
    c = int(input('Enter your choice:'))
    if c == 1:
        name = str(input(Fore.LIGHTGREEN_EX + 'What is the name of the password:'))
        names = read_file_list('names.txt')
        if name in names:
            print("\n")
            print(Fore.RED + 'The name already exists.')
        else:
            password = str(input(Fore.LIGHTGREEN_EX + 'What is the password:'))
            key = str(input('What is the key to encrypt the password:'))
            print('\n')
            store_password(name,password,key)
    elif c == 3:
        name = str(input(Fore.LIGHTGREEN_EX + 'What is the name of the password:'))
        names = read_file_list('names.txt')
        if name not in names:
            print("\n")
            print(Fore.RED + "This name does not exist.")
        else:
            oldpass = str(input(Fore.LIGHTGREEN_EX + 'What is your old password:'))
            oldkey = str(input('What is your old key:'))
            passwords = read_file_list('password.txt')
            if oldpass != decryF(passwords[names.index(name)],oldkey):
                print("\n")
                print(Fore.RED + 'The old password or old key is incorrect.')
            else:
                newpass = str(input(Fore.LIGHTGREEN_EX + 'What is your new password:'))
                newkey = str(input('What is your new key:'))
                result = update_password(name,oldpass,newpass,oldkey,newkey)
                if result == 'The update is successful.':
                    print("\n")
                    print(Fore.LIGHTBLUE_EX + result)
                    password_stren(newpass)
                else:
                    print(result)
    elif c == 2:
        name = str(input(Fore.LIGHTGREEN_EX + 'What is the name of the password:'))
        names = read_file_list('names.txt')
        if name not in names:
            print("\n")
            print(Fore.RED + "The name does not exit.")
        else:
            key = str(input(Fore.LIGHTGREEN_EX + 'What is the key:'))
            password = retrieve_password(name,key)
            if password == 'This name does not exist.':
                print(password)
            else:
                print("\n")
                print(Fore.LIGHTBLUE_EX + 'The password is:' + Fore.LIGHTCYAN_EX, password)
                pyperclip.copy(password)
                print(Fore.LIGHTBLUE_EX + 'The password is copied to your clipboard.')
    elif c == 4:
        password = str(input(Fore.LIGHTGREEN_EX + 'Enter a password:'))
        print('\n')
        password_stren(password)

    elif c == 5:
        password = password_generator()
        print('\n')
        print(Fore.LIGHTBLUE_EX + 'The random password is:' + Fore.LIGHTCYAN_EX, password)
        pyperclip.copy(password)
        print(Fore.LIGHTBLUE_EX + 'The random number is copied to your clipboard.')
    elif c == 6:
        sys.exit()
    else:
        print(Fore.RED + 'Your choice is invalid.')


while True:
    if __name__ == '__main__':
        main()
