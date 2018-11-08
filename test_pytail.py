import os

from pytail import tail_from


def test_tail_from_1line_n1():
    full_file_path = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files/test-utf8-1line.txt'))

    tail_output = None
    with open(full_file_path, 'r') as f:
        tail_from(f, lines_remaining=1)
        tail_output = f.readlines()

    assert tail_output[0] == '1abc'


def test_tail_from_5line_n5():
    full_file_path = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files/test-utf8-5line.txt'))

    tail_output = None
    with open(full_file_path, 'r') as f:
        tail_from(f, lines_remaining=5)
        tail_output = f.readlines()

    assert tail_output[0] == '1abc\n'
    assert tail_output[1] == '2abc\n'
    assert tail_output[2] == '3abc\n'
    assert tail_output[3] == '4abc\n'
    assert tail_output[4] == '5abc'
