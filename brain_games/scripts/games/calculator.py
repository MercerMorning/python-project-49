import prompt
import random


def main():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    operators = ['+', '-', '*']
    right_answer_count = 0
    while (right_answer_count != 3):
        if (ask(random.randint(0, 22), random.randint(0, 22), random.choice(operators))):
            right_answer_count += 1
    print(f'Congratulations, {name}!')


def ask(first_number, second_numer, operator):
    expression = f'{first_number} {operator} {second_numer}'
    print('Question: ' + expression)
    if int(prompt.string('Your answer: ')) == eval(expression):
        print('Correct!')
        return True
    return False
