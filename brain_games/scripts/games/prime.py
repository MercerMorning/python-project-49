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
    print(f'Congratulations, {name}!')


def ask(number):
    print(f'Question: {number}')
    is_prime_number = 'yes' if is_prime(number) else 'no'
    if (prompt.string('Your answer: ') == is_prime_number):
        print('Correct!')
        return True
    return False


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n
