import random

tasks: int = 0
correct: int = 0

while True:

    print("""
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
""", end='')

    try:
        difficulty: int = int(input())
        if difficulty not in (1, 2):
            print('Incorrect format')
            continue
        break
    except ValueError:
        print("Incorrect format")
        continue

while tasks < 5:

    if difficulty == 1:

        opps: str = ('+', '-', '*')

        simple: tuple = tuple(range(2, 10))

        first, second, opp = str(random.choice(simple)), str(random.choice(simple)), random.choice(opps)

        print(first, opp, second)

        while True:
            try:
                answer: int = int(input())
                break
            except ValueError:
                print("Incorrect format")
                continue

        if opp == '+':
            actual: int = int(first) + int(second)
        elif opp == '-':
            actual: int = int(first) - int(second)
        elif opp == '*':
            actual: int = int(first) * int(second)

        if answer == actual:
            print('Right!')
            correct += 1
        else:
            print('Wrong!')

    elif difficulty == 2:

        squares: tuple = tuple(range(11, 30))

        square: int = random.choice(squares)

        print(square)

        while True:
            try:
                answer: int = int(input())
                break
            except ValueError:
                print("Incorrect format")
                continue

        if answer == square ** 2:
            print('Right!')
            correct += 1
        else:
            print('Wrong!')

    tasks += 1

print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.")

save: str = input().upper()

if save in ('Y', 'YES'):
    print("What is your name?")
    name: str = input()

    if difficulty == 1:
        message: str = '(simple operations with numbers 2-9)'
    elif difficulty == 2:
        message: str = '(integral squares 11-29)'

    with open('results.txt', 'a') as results:
        results.write(f'{name}: {correct}/5 in level {difficulty} {message}.')

    print('The results are saved in "results.txt".')
