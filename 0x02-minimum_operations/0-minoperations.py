#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    if n <= 0:
        return 0
    add = 'H'
    body = 'H'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            add = body
            body += body
        else:
            op += 1
            body += add
    if len(body) != n:
        return 0
    return op
