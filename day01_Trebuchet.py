"""
day01_Trebuchet.py

--tkp

Advent of Code puzzle Day 1
Source: https://adventofcode.com/2023/day/1

Instructions:
-------------
... The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

import string



def get_digits_value(instr):
    digits = [d for d in instr if d in string.digits]
    retval = 0 if len(digits) == 0 else int(digits[0] + digits[-1])
    return retval


def test():
    lines = ['1abc2','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet']
    assert sum([get_digits_value(line) for line in lines]) == 142


if __name__ == "__main__":
    test()
    lines = open('./input_day01.txt').readlines()
    calibration = sum([get_digits_value(line) for line in lines])
    print(calibration) 
