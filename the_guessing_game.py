import numpy as np

GAMES = []

def menu_game():
    ans = ''
    while True:
        random_number = np.random.randint(low=100, high=1000)
        count = 0
        while(1):
            guess_number = input('Your guess? ')
            is_number = guess_number.isnumeric()
            is_in_range = is_number and int(guess_number) in range(100, 1000)
            valid_input = is_in_range and is_number
            if valid_input:
                guess_number = int(guess_number)
                count += 1
                if guess_number == random_number:
                    print('You got it right in ' + str(count))
                    print('Credits: {}'.format(compute_credit(count)))
                    break
                times = check(guess_number, random_number) 
                where = 'higher' if guess_number > random_number else 'lower'
                print("It's {}".format(where))
                print("Matched {} numbers".format(times))
            else:
                if guess_number == 'exit':
                    return 0
                if not is_in_range:
                    print('Input must be in range 100 -> 999')
                if not is_number:
                    print('Input must be a number')

        ans = input('Play again? ')
        while ans not in ['yes', 'no','y','n']:
            print('Wrong answer!')
            ans = input('Playe again? ')
        GAMES.append(count)
        if ans == 'no' or ans == 'n':
            return 1


def check(guess_number, random_number):
    random_digits = split_number(random_number)
    guess_digits = split_number(guess_number)
    count = 0
    return len(np.intersect1d(random_digits, guess_digits))

def compute_credit(count):
    if count in range(1, 5):
        return 60
    return 10

def split_number(n):
    digits = []
    while n > 10:
        digits.append(n % 10)
        n = n // 10
    digits.append(n)
    return np.array(digits)

if __name__ == '__main__':
    print('         ---G U E S S I N G   G A M E---            ')
    print('                     LET\'S PLAY                    ')
    print(' Try to guess my three-digit combination, and I will tell you if any your numbers match my combination.')
    print(' Credits')
    print('                                   1-4 Guesses: up to 60 credits')
    print('                                   5-10 Guesses: 10 credits')

    menu_game()
    results = np.array(GAMES)
    credits = list(map(compute_credit, results))
    print('Overal results:')
    print('Total games = {}'.format(len(GAMES)))
    print('Total guess = {}'.format(results.sum()))
    print('Guesses/game = {}'.format(results.mean()))
    print('Best game = {}'.format(results.argmax() + 1))
    print('Total credits = {}'.format(sum(credits)))