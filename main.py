'''
>>> JAAR
>>> 09/11/2023
>>> Practicing Fundamentals Program 21
>>> Version 1
'''

'''
>>> Prompts the user to create a new file, rename an existing file, or to check if a file they are trying to open exists.
'''

import os

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
    actions = [1, 2, 3]
    print('''
        (1) Create a file.
        (2) Check if a file exists.
        (3) Change the name of an existing file.
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

def file_name_input(string = ' ') :
    '''
    >>> Asks the user to input a file name. Then asks the user to verify their input before it returns the user input.
    >>> Return: (file) file_name
    '''
    while True :
        file_name = input(f'Enter a{string}file name: ')
        print(f"Your input was: '{file_name}'")
        response = user_response('Is your input correct')
        if response == 'yes' :
            return file_name

def main() :
    response = 'yes'
    while response == 'yes' :
        action = user_action()
        file = file_name_input()
        if action == 1 :
            with open(f'{file}.txt', 'w') as f:
                print(f'{file}.txt was created ')
        elif action == 2 :
            try :
                with open(file, 'r') as f :
                    print(f'file {f.name()} exists.')
            except IOError as e :
                print(f"file {file} doesn't exist.")
        else :
            rename = file_name_input(string = ' new ')
            os.rename(file, f'{rename}.txt')
        response = user_response('Do you want to take another action?')

if __name__ == '__main__' :
    main()