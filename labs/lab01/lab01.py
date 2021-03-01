"""Lab 1: Expressions and Control Structures"""


def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0  # You can replace this line!


def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    "*** YOUR CODE HERE ***"
    # digits = [int(n) for n in str(n)]
    # return sum(digits)

    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum
