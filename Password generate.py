import string
import random

def password(userinput):
    if userinput == 'strong':
        return ''.join(random.choice(string.hexdigits + string.punctuation) for i in range(16))
    elif userinput == 'week':
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
#string.hexdigits: The string '0123456789abcdefABCDEF'
#string.punctuation: String of ASCII characters which are considered punctuation characters in the C locale.


def replay():
    return input('Do you want to generate again? Y or N: ').lower().startswith('y')

while True:
    userinput= input('Do you want strong password or week passowrd:')
    print(password(userinput))
    if replay() == False:
        break
