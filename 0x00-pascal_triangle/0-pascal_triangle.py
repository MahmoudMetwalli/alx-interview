#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """Return a list os lists representing the pascal triangle"""
    list_of_lists = []
    if n <= 0:
        return list_of_lists
    for i in range(0, (n + 1)):
        list_of_lists.append([])
        for j in range(0, i):
            if j == 0 or j == (i - 1):
                list_of_lists[i].append(1)
            else:
                list_of_lists[i].append(
                    (list_of_lists[i - 1][j - 1] + list_of_lists[i - 1][j]))
    list_of_lists.pop(0)
    return list_of_lists
