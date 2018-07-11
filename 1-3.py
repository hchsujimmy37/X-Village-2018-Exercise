import random
correct=random.randint(1,101)
answer=int(input('Enter a number :'))
while correct!=answer:
    if answer<0 or answer>100:
        print('You input the wrong answer.')
        answer=int(input('Enter a number again :'))
    elif answer>correct:
        print('Too big')
        answer=int(input('Enter a number again :'))
    elif answer<correct:
        print('Too small')
        answer=int(input('Enter a number again :'))
print('Correct!')
