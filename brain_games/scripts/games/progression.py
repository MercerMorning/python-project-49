import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    right_answer_count = 0
    while (right_answer_count != 3):
        if (ask(random.randint(0, 22), random.randint(0, 22))):
            right_answer_count += 1
        else:
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')


def ask(first_number, second_numer):
    progression, space_value = generate_progression()
    print(f'Question: {progression}')
    if (int(prompt.string('Your answer: ')) == space_value):
        print('Correct!')
        return True
    return False


def generate_progression():
    current_number = random.randint(0, 22)
    progression_length = 9
    progression_space_index = random.randint(0, progression_length)
    index = 0
    progression = str(current_number)
    step = random.randint(1, 9)
    space_value = ''
    while index < progression_length:
        current_number += step
        if (progression_space_index == index):
            space_value = current_number
            progression += ' ..'
        else:
            progression += f' {current_number}'

        index += 1
    return (progression, space_value)
