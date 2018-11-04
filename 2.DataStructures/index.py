import sys

from collections import deque

def main():
    print('Data Structures !!')

    # More on lists
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    print(fruits.count('apple'))
    print(fruits.count('tangerine'))
    print(fruits.index('banana'))
    print(fruits.index('banana', 4))    # find next banana starting a position 4
    fruits.reverse()
    print(fruits)
    fruits.append('grape')
    print(fruits)
    fruits.sort()
    print(fruits)
    print(fruits.pop())

    print("\n")

    # Using lists as stacks
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack)

    print("\n")

    # Usign lists as queues
    queue = deque(['Eric', 'John', 'Michael'])
    print(queue)
    queue.append('Terry')
    queue.append('Graham')
    print(queue.popleft())
    print(queue.popleft())
    print(queue)

    print("\n")

    # List comprehensions
    squares = []
    for x in range(10):
        squares.append(x**2)
    print(squares)

    print("\n")

    # equivalent to
    squares = [x**2 for x in range(10)]
    print(squares)

    # other examples
    vec = [-4, -2, 0, 2, 4]
    # creates a new list with the values dubled
    print([x*2 for x in vec])
    # filter the list to exclude negative values
    print([x for x in vec if x >= 0])
    # apply a function to all the elements
    print([abs(x) for x in vec])
    # call a method on each element
    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    print([fruit.strip() for fruit in freshfruit])
    # create a list of 2-tuples like (number, square)
    print([(x, x**2) for x in range(6)])
    # flatten a list using a listcomp with two 'for'
    vec = [[1,2,3], [4,5,6], [7,8,9]]
    print([num for elem in vec for num in elem])

    print("\n")

    # Nested list comprehensions
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    print([[row[i] for row in matrix] for i in range(4)])

    print("\n")

    # The del statement
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]
    print(a)
    del a[2:4]
    print(a)
    del a[:]
    print(a)




if __name__ == '__main__':
    main()