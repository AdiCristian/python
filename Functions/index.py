import sys

# Default argument values
def ask_ok(prompt, retries = 4, reminder = 'Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            print('Ok')
        if ok in ('n', 'nop', 'nope'):
            print('Not Ok')
        
        retries = retries - 1
        if retries < 0:
            return False
        print(reminder)

# Keyword Arguments
def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
    print('-- This parrot wouldn\'t', action, end = ' ')
    print('if you put', voltage, 'volts through it.')
    print('-- Lovely plumage, the', type)
    print('-- It\'s', state, '!')

# Get all arguments and keywords of the method
def cheeseshop(kind, *arguments, **keywords):
    print('-- Do you have any', kind)
    print('-- I\'m sorry, we\'re all out of', kind)

    for arg in arguments:
        print(arg)
    
    print('-' * 40)

    for kw in keywords:
        print(kw, ':', keywords[kw])

def my_function():
    """
    Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

def main():
    print('About functions !!')

    ask_ok('Do you really want to quit ?', 0)
    ask_ok('Ok to overwrite the file ?', 0)
    ask_ok('Ok to overwrite the file ?', 0, 'Come on, only yes or no !')

    print("\n")

    parrot(1000)
    parrot(voltage = 1000)
    parrot(voltage = 1000000, action = 'VOOOOOM')
    parrot(action = 'VOOOOOM', voltage = 1000000)
    parrot('a million', 'bereft of life', 'jump')
    parrot('a thousand', state = 'pushing up the daisies')

    """
    The following calls are invalid    
        parrot()                     # required argument missing
        parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
        parrot(110, voltage=220)     # duplicate value for the same argument
        parrot(actor='John Cleese')  # unknown keyword argument
    """

    print("\n")

    cheeseshop("Limburger", "It's very runny, sir.",
            "It's really very, VERY runny, sir.",
            shopkeeper="Michael Palin",
            client="John Cleese",
            sketch="Cheese Shop Sketch")

    print("\n")

    print(my_function.__doc__)


if __name__ == '__main__':
    main()