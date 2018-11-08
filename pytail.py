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


def tail_from(f, num_lines):
    """
    Sets the file's current position to the point from which to print the tail output, given the number of lines to print.
    It is assumed the file has already been opened with mode 'r'.
    :param f: file
    :param num_lines: the number of lines to tail
    :return: nothing; instead sets the file cursor to the point to tail from
    """
    # Seek to end of file, reading from here will give us '', so we'll start our loop by backing up 1 char
    f.seek(0, os.SEEK_END)

    # While there is still a positive number of lines to tail and we're not at the beginning of the file,
    # move the cursor back one character, read that character and check to see if it is a line separator.
    while num_lines > 0 and f.tell() > 0:
        f.seek(f.tell() - 1, os.SEEK_SET)
        ch = f.read(1)
        if ch == os.linesep:
            num_lines -= 1
        if num_lines > 0:
            # Back up an additional character because reading moved our cursor forward (1 forward, 2 back each iteration)
            f.seek(f.tell() - 1, os.SEEK_SET)


def main():
    args = get_input_args()

    full_file_path = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), args.file_path))

    with open(full_file_path, 'r') as f:
        tail_from(f, int(args.num_lines))
        shutil.copyfileobj(f, sys.stdout)


if __name__ == "__main__":
    main()
