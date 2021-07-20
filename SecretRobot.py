command = ''
user_name = input('Enter name: ')
secret_number = 64
tries = 0
tries_limit = 8

print(f'Welcome {user_name}, i am "SecretRobot64". Nice to meet you.')
while True:
    command = input('>').lower()
    if command == 'hello':
        print('How are you today?')
        command = input('>').lower()
        if command == 'good':
            print('Great! Lets begin')
    else:
        print('Nice modals...well lets begin.')
    while tries <= 8:
        guess = int(input('Guess the SECRET number im "thinking"of...: '))
        tries += 1
        if guess == secret_number:
            print(f'''Well well well, it seems as if you have guessed it right. In 19{secret_number}, 
            my creator s father was born. Nice little touch if i may say so...
            All in all, I "wish" you a great day. See you soon'
            ''')
            break
    else:
        print('You lose. Good luck next time!')
        break
    break
while True:
    command = input('>').lower()
    if command == 'quit':
        break
    else:
        print('...if your were so kind to write "quit"...')






