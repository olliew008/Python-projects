import random


def main():
    comp = random.randrange(1,100)
    count = 0
    guesses = 4
    print('you have 5 guesses')
    while True:
        
        
        uguess = int(input('Put a number idk: '))
        print('You have', guesses - count, 'guesses left' )

        if guesses == 0:
            break

        if uguess == comp:
           print('yayyy', 'It took', count, 'attempts')
           break

        elif uguess < comp:
            count += 1
            print('too small..')

        elif uguess > comp:
            count += 1
            print('massive')

main()