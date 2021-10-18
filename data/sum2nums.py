#!/usr/bin/env python

usage = '''python sum2nums.py number1 number2'''
import sys
def sum2num(num1,num2):
    return num1+num2
if __name__ == '__main__':
    try:
        number1 = float(sys.argv[1])
        number2 = float(sys.argv[2])
        print('The sum of the numbers is: {0}'.format(sum2num(number1,number2)))
    except:
        print(usage)