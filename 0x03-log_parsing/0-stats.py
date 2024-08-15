#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys


def print_metrics(total, codes_dict):
    """print metrics"""
    print(f"File size: {total}")
    for key2, value2 in codes_dict.items():
        if value2:
            print(f"{key2}: {value2}")


if __name__ == "__main__":

    codes_list = ['200', '301', '400', '401', '403', '404', '405', '500']
    codes_dictionary = {'200': 0, '301': 0, '400': 0,
                        '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    COUNT = 0
    TOTAL_FILE_SIZE = 0
    try:
        for line in sys.stdin:
            try:
                if (line.split())[-2] in codes_list:
                    codes_dictionary[(line.split())[-2]] += 1
            except IndexError:
                pass
            try:
                TOTAL_FILE_SIZE += int((line.split())[-1])
            except (IndexError, ValueError):
                pass
            COUNT += 1
            if COUNT == 10:
                print_metrics(TOTAL_FILE_SIZE, codes_dictionary)
                COUNT = 0
        print_metrics(TOTAL_FILE_SIZE, codes_dictionary)
    except KeyboardInterrupt:
        print_metrics(TOTAL_FILE_SIZE, codes_dictionary)
        raise
