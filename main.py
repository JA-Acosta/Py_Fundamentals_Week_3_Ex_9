'''
>>> JAAR
>>> 09/11/2023
>>> Practicing Fundamentals Program 21
>>> Version 2
'''

'''
>>> Prompts the user to create a new file, rename an existing file, or to check if a file they are trying to open exists.

>>> Append: Asks the user to enter a file, if the file exists, deletes the file or lets the user know the file doesn't exist.
'''

import os
import re

def user_response(question)->str :
    '''
    >>> asks the user to enter either yes or no. Otherwise, prompts the user to input another response. Then returns the user response.
    >>> Returns: (str) response
    '''
    response = ''
    while True :
        response = input(f'{question} (yes/no): ').lower()
        if response == 'yes' or response == 'no' :
            return response
        else :
            print('Your response was invalid.', end = '')

def user_action()-> int :
    '''
    >>> Asks the user to enter an action they'd like to take. If the user enters an invalid response, prompts the user to enter another response.
    >>> Return: (int) action
    '''
    actions = [1, 2, 3, 4]
    print('''
        (1) Create a file.
        (2) Check if a file exists.
        (3) Rename an existing file.
        (4) Delete a file.
    ''')
    action = ''
    while action not in actions :
        try :
            action = int(input('Enter your response: '))
            if action not in actions :
                raise ValueError
        except ValueError :
            print('Enter a valid response. ', end = '\n\t')
        else :
            return action

def file_path_input(string = ' ', path = 'path') :
    '''
    >>> Asks the user to input a file name. Then asks the user to verify their input before it returns the user input.
    >>> Return: (file) file_name
    '''
    while True :
        file_path = input(f'Enter a{string}file {path}: ')
        print(f"Your input was: '{file_path}'")
        response = user_response('Is your input correct')
        if response == 'yes' :
            return file_path

def main() :
    response = 'yes'
    while response == 'yes' :
        action = user_action()
        file_name = ''
        if action == 1 :
            file_name = file_path_input(path = 'name')
        else :
            file_path = file_path_input()
            file_name = re.search(r'[a-zA-Z0-9._-]+\.txt', file_path).group()
        if action == 1 :
            with open(f'{file_name}.txt', 'w') as f:
                print(f'{file_name}.txt was created ')
        elif action == 2 :
            if os.path.exists(file_path) :
                print(f'{file_name} exists.')
            else :
                print(f"{file_name} doesn't exist.")
        elif action == 3 :
            rename = file_path_input(string = ' new ')
            os.rename(file_path, f'{rename}.txt')
        else :
            try :
                os.remove(file_path)
                print(f'{file_name} was deleted.')
            except OSError :
                print(f"{file_name} doesn't exist.")
        response = user_response('Do you want to take another action?')

if __name__ == '__main__' :
    main()