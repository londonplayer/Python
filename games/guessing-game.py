import random

result = random.randint(0,9)

print('Guess the number between 1 and 10: ')
print(result)

guess = int(input())

if guess == result:
    print('Correct!')
else:
    print('Wrong answer! The correct number is ' + str(result))

print(guess)