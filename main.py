from random import choice


def random_fruit():
    list_fruits = [
        'apple', 'banana', 'orange', 'lemon', 'kiwi', 'pineapple', 'watermelon', 'grape', 'pear', 'mango', 'avocado',
        'melon', 'peach', 'tangerine', 'nectarine', 'papaya', 'plum', 'pomelo', 'pomegranate', 'apricot'
    ]
    choice_fruit = choice(list_fruits).lower()
    return choice_fruit


fruit = random_fruit()
secret_word = '*' * len(fruit)
guessed_letters = list()

user_attempts = int(input('Enter the number of attempts: '))

while user_attempts > 0:
    user_input = input('Enter a word or letter: ').lower()

    if len(user_input) == 1:
        if user_input in fruit:
            if user_input not in guessed_letters:
                guessed_letters.append(user_input)
                secret_word = ''.join([user_input if user_input in guessed_letters else '*' for user_input in fruit])
                print(secret_word)
                if '*' not in secret_word:
                    print('Congratulations, you guessed the word!')
                    break
            else:
                print('You have already entered this letter!')
        else:
            print('This letter is not in the word!')
            user_attempts -= 1
    elif user_input == fruit:
        print('Congratulations, you guessed the word!')
        break
    else:
        print('Not true. Enter a single letter or word!')
        user_attempts -= 1
