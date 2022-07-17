import random

print("Hi, do you wanna play Rock, Paper, Scissors? You can always enter stop when tired...")

def  game():
    
    choices = ('Paper. Rock , Scissors')
    print(choices)


    com_choice = random.choice(choices)


    number_of_trail = 5
    guess = 0
    point = 5

    condition = 'Stop!'

    while guess < number_of_trail:

        user_input = input('Enter guess choice to play: ')

        print(user_input)

        
        
        if user_input == 'SCISSORS' and com_choice.upper() == 'PAPER':
            print('You win, You get one more try')
            point+=1
            print(f'your score is {point}')
            number_of_trail+=1
        
        
        
        elif user_input.upper() == 'ROCK' and com_choice.upper() == 'SCISSORS':
            print('You win, You get one more try')
            point+=1
            print(f'your score is {point}')

        
        elif user_input.upper() == condition.upper():
            print("Game Stopped")
            exit()

        
        elif user_input.upper() == 'PAPER' and com_choice.upper() == 'ROCK':
            print('You win, You get one more try')
            point+=1
            print(f'your score is {point}')
            number_of_trail+=1
        
        elif user_input.upper() == com_choice.upper():
            print('Its a tie')

        elif user_input.upper() == 'ROCK' and com_choice.upper() == 'PAPER' :
            number_of_trail-=1
            print('You lose, You lost a trial')
        
        elif user_input.upper() == 'SCISSORS' and com_choice.upper() == 'ROCK':
            number_of_trail-=1
            print('You lose, You lost a trial')
        
        elif user_input.upper() == 'PAPER' and com_choice.upper() == 'SCISSORS':
            number_of_trail-=1
            print('You lose, You lost a trial')

        else:
            print('You lose, try again')
        
        
        print(com_choice)
        guess += 1
    
    else:
        print('You are out of choices')
        x= input('Do you wish to continue playing?    Enter Yes or No').upper()
        if x =='YES':
            game()
        else:
            print('Goodbye!')
            exit()

game()
        
        
        