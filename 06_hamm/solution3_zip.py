#!/usr/bin/env python3
""" Hamming distance """

import argparse
import sys
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='File input')

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    lines = args.file.read().splitlines()

    if len(lines) != 2:
        sys.exit(f'Input file "{args.file.name}" must have two lines.')

    print(hamming(*lines))


# --------------------------------------------------
def hamming(seq1: str, seq2: str) -> int:
    """ Calculate Hamming distance """

    # Method 2: The base distance is the difference in their lengths
    distance = abs(len(seq1) - len(seq2))

    # Use zip to pair up the letters
    for char1, char2 in zip(seq1, seq2):
        if char1 != char2:
            distance += 1

    return distance


# --------------------------------------------------
def test_hamming() -> None:
    """ Test hamming """

    assert hamming('', '') == 0
    assert hamming('AC', 'ACGT') == 2
    assert hamming('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT') == 7


# --------------------------------------------------
if __name__ == '__main__':
    main()
