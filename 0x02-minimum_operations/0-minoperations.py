#!/usr/bin/python3
"""
Calculate minimum operations for printing a number fo characters
"""


def minOperations(n):
    """Calculate minimum operations for printing a number fo characters"""
    if n <= 0:
        return 0
    k = 1
    while n % 2 == 0:
        k = k * 2
        n = n // 2
    if k == 1:
        return n
    if n > 1:
        return k + n
    if n == 1:
        return k
