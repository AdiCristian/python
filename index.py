import sys


# Write Fibbonacci series up to n
def fib(n):
    a, b = 0, 1

    while a < n:
        print(a, end=' ')
        a, b = b, a + b


# Return a list containing Fibonacci series up to n
def fib2(n):
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)
        a, b = b, a + b

    return result


def main():
    # if else Statement
    x = int(input('Please enter an integer: '))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

    # for Statement

    # Measure some strings:
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

    # The range() Funciton
    for i in range(5):
        print(i)

    # break and continue Statements,
    # and else Clauses on loops
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n // x)
                break
        else:
            print(n, 'is a prime number')

    for num in range(2, 10):
        if num % 2 == 0:
            print('Found an even number', num)
            continue
        print('Found a number', num)

    fib(2000)

    print(fib2(2000))


if __name__ == "__main__":
    main()
