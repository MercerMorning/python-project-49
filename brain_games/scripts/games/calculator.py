import prompt
import random


def main():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    right_answer_count = 0
    while (right_answer_count != 3):
        if (ask()):
            right_answer_count += 1
    print(f'Congratulations, {name}!')


def ask():
    operators = ['+', '-', '*']
    first_number = random.randint(0, 22)
    second_numer = random.randint(0, 22)
    operator = random.choice(operators)
    expression = f'{first_number} {operator} {second_numer}'
    print('Question: ' + expression)
    answer = prompt.string('Your answer: ')
    expr_res = eval(expression)
    if int(answer) == expr_res:
        print('Correct!')
        return True
    text = f"'{answer}' is wrong answer ;(. Correct answer was '{expr_res}'."
    print(text)
    return False
