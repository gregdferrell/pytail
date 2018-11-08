#!/usr/bin/env python3

import argparse
import os
import shutil
import sys


def get_input_args():
    """
    Retrieves and parses the command line arguments created and defined using the argparse module.
    :return: parse_args() -data structure that stores the command line arguments object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="the path to the file to tail")
    parser.add_argument("-n", "--num-lines", help="the number of lines to print", default=5)

    args = parser.parse_args()

    return args


def tail_from(f, lines_remaining):
    f.seek(0, os.SEEK_END)
    while lines_remaining > 0:
        try:
            f.seek(f.tell() - 1, os.SEEK_SET)
        except ValueError:
            # If we get to beginning of file, break
            break
        ch = f.read(1)
        if ch == os.linesep:
            lines_remaining -= 1
        if lines_remaining > 0:
            f.seek(f.tell() - 1, os.SEEK_SET)


def main():
    args = get_input_args()

    full_file_path = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), args.file_path))

    with open(full_file_path, 'r') as f:
        tail_from(f, int(args.num_lines))
        shutil.copyfileobj(f, sys.stdout)


if __name__ == "__main__":
    main()
