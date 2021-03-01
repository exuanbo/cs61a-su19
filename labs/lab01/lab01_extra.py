"""Optional questions for Lab 1"""

# While Loops


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    product = 1
    while k > 0:
        product *= n
        n -= 1
        k -= 1
    return product


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    is_last_digit_eight = False
    while n != 0:
        digit = n % 10
        if digit == 8:
            if is_last_digit_eight:
                return True
            is_last_digit_eight = True
        else:
            is_last_digit_eight = False
        n //= 10
    return False
