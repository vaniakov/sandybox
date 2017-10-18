#! /usr/bin/python
from __future__ import print_function
import argparse
import time


CHARS_FROM_END = 500

def tail(file_name, read_from_end):
    with open(file_name, 'r') as f:
        end_position = f.seek(0, 2) or 0
        f.seek(max(0, end_position - read_from_end)) 
        while True:
            try:
                new_line = f.readline()
                if new_line:
                    yield new_line
                else:
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print('Exiting tail..')
                break


def main():
    parser = argparse.ArgumentParser(description='Stream reader.')
    parser.add_argument('file_name', help='file name to tail')
    parser.add_argument('-n', '--num_chars', help='Read num chars from the end'
                        'of the file', default=CHARS_FROM_END)
    args = parser.parse_args()
    print(args)

    for line in tail(args.file_name, args.num_chars):
        print(line, end='')


if __name__ == '__main__':
    main()
