import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    right_answer_count = 0
    while (right_answer_count != 3):
        if (ask(random.randint(1, 22), random.randint(1, 22), name)):
            right_answer_count += 1
        else:
            return
    print(f'Congratulations, {name}!')


def ask(first_number, second_numer, name):
    print(f'Question: {first_number} {second_numer}')
    gcd = find_gcd(first_number, second_numer)
    answer = prompt.string('Your answer: ')
    if int(answer) == gcd:
        print('Correct!')
        return True
    print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{gcd}\'.
Let's try again, {name}!''')
    return False


def find_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
