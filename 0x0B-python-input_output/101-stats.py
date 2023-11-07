#!/usr/bin/python3
"""stats"""
from sys import stdin


def print_stats(size, cnt):
    """stdin"""
    print("File size: {}".format(size))
    for status_code in sorted(cnt.keys()):
        if cnt[status_code] > 0:
            print("{}: {}".format(status_code, cnt[status_code]))

def main():
    try:
        line = 0
        size = 0
        cnt = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0,
        }

        for data in sys.stdin:
            line += 1
            parts = data.split()
            if len(parts) >= 7:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                size += file_size
                if status_code in cnt:
                    cnt[status_code] += 1
            if line % 10 == 0:
                print_stats(size, cnt)
    except KeyboardInterrupt:
        print_stats(size, cnt)

