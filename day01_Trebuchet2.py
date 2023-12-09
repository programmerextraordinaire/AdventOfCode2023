"""
day01_Trebuchet.py

--tkp

Advent of Code puzzle Day 1
Source: https://adventofcode.com/2023/day/1#part2

Instructions:
-------------
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

import string


def get_digits_value(instr):
    digits = [d for d in instr if d in string.digits]
    retval = 0 if len(digits) == 0 else int(digits[0] + digits[-1])
    return retval


def str2digits(instr):
    retstr = '' 
    d = {
         'eighthree':'83',
         'threeight':'38',
         'fiveight':'58',
         'nineight':'98',
         'sevenine':'79',
         'eightwo':'82',
         'oneight':'18',
         'twone':'21',
         'one':'1', 
         'two':'2', 
         'three':'3', 
         'four':'4', 
         'five':'5', 
         'six':'6', 
         'seven':'7', 
         'eight':'8', 
         'nine':'9', 
         'zero':'0'
         }
    # Loop through and skip matches.
    i = 0
    while i < len(instr):
        notFound = True
        for key in d:
            keylen = len(key)
            if instr[i:i+keylen] == key:
                retstr += d[key]
                i += keylen
                notFound = False
                break
        if notFound:
            retstr += instr[i]
            i += 1
    return retstr 

def test():
    lines = ['1abc2','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet']
    assert sum([get_digits_value(line) for line in lines]) == 142

def test2():
    lines = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()
    assert sum([get_digits_value(str2digits(line)) for line in lines]) == 281
 

if __name__ == "__main__":
    test()
    test2()
    lines = open('./input_day01.txt').readlines()
    calibration = sum([get_digits_value(str2digits(line)) for line in lines])
    print(calibration) 
