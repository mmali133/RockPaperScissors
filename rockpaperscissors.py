import random

while True:
    usr_command = input('Enter your command: ').lower()
    possible = ['rock', 'paper', 'scissors']
    com_action = random.choice(possible)
    if usr_command == com_action:
        print(f'Opponent chose {com_action}')
        print(f'Both players selected {usr_command}. Its a tie!')
    elif usr_command == 'rock':
        print(f'Opponent chose {com_action}')
        if com_action == 'scissors':
            print('Rock beats scissors. You win!')
        else:
            print('Womp Womp you loose')
    elif usr_command == 'scissors':
        print(f'Opponent chose {com_action}')
        if com_action == 'paper':
            print('Scissors cuts paper. You win!')
        else:
            print('Womp Womp you loose')
    elif usr_command == 'paper':
        print(f'Opponent chose {com_action}')
        if com_action == 'rock':
            print('Paper sufficates rock. You win!')
        else:
            print('Womp Womp you loose')
    elif usr_command == 'help':
        print('''
You must choose an option from below to play the game.
Rock
Paper
Scissors
        ''')
    else:
        print('Im sorry I did not understand that input. Please either type in rock, paper, or scissors')
    if usr_command == 'quit':
        break