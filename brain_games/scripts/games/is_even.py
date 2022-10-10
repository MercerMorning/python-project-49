import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answer_count = 0
    while (right_answer_count != 3):
        if (ask(random.randint(0, 22))):
            right_answer_count += 1
        else:
            right_answer_count = 0
    print(f'Congratulations, {name}!')


def ask(number):
    print(f'Question: {number}')
    is_even_number = 'yes' if number % 2 == 0 else 'no'
    if (prompt.string('Your answer: ') == is_even_number):
        print('Correct!')
        return True
    return False
