import random
import time
affirm = ['yes', 'y', 'ye']

def main():

    print('Guessing Game')
    time.sleep(1)
    print(' _---_')
    print('/     |')
    print('      |')
    print('     |')
    print('    |')
    print('    |')
    print('     ')
    print('    O')
    time.sleep(0.5)

    cus_game = input('Custom game? ')

    if cus_game in affirm:

        x = int(input('Enter first value of the range: '))
        y = int(input('Enter second value of the range: '))
    
    else:
        x = 1
        y = 100

    comp = random.randrange(x,y)
    count = 0
    guesses = 4
    print('you have 5 guesses')
    time.sleep(0.25)
    print('Guess between the range of', x, 'and', y)
    while True:
        
        gleft = guesses - count
        
        uguess = int(input('Put a number idk: '))
        print('You have', gleft, 'guesses left' )

        if gleft <= 0:
            print('game over')
            time.sleep(1)
            break

        if uguess == comp:
           print('yayyy', 'It took', count, 'attempts')
           time.sleep(2)
           break

        elif uguess < comp:
            count += 1
            print('too small..')

        elif uguess > comp:
            count += 1
            print('massive')

main()