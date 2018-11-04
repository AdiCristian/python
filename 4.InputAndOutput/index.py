import sys
import math
import json

def main():

    # Fancier output formating
    print("Input and Output chapter !!")

    print(f'The value of pi is approximately {math.pi:.3f}')

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

    for name, phone in table.items():
        print(f'{name:10} ===> {phone:10d}')

    # Basic usage of str.format() method
    print('We are the {} who say "{}!"'.format('knights', 'Ni'))
    print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

    # Reading and writing files
    with open('workfile') as f:
        read_data = f.read()

    print(f.closed)

    # Saving structured data with json
    f = open('workfile', 'w')
    x = [1, 'simple', 'list']
    json.dump(x, f)
    f.close()

    f = open('workfile')
    print(json.load(f))
    f.close()


if __name__ == '__main__':
    main()

