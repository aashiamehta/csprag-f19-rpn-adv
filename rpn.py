#!/usr/bin/env python3

import operator
import readline
from colored import fg, bg, attr


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

color = bg('indian_red_1a') + fg('white')
reset = attr('reset')

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("%s Result: %s" % (fg('indian_red_1a'), attr(0)), result)
        print(color + "Thanks for using this calculator!" + reset)

if __name__ == '__main__':
    main()
