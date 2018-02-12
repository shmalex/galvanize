""" Task 5 : 
Write a function called calculator. 
It should take the following parameters: 
A)two numbers, and
B)an arithmetic operation (which can be addition, subtraction, multiplication or division)
The function should perform the requested operation on the two input numbers, 
Raise exceptions as appropriate if any of the parameters passed to the function are invalid.\
Use enum and/or dictionaries as needed to solve this task
"""
import math


def opt_sum(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(a + b)


def opt_minus(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(a - b)


def opt_div(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(a / b)


def opt_mult(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(a * b)


def opt_pow(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(math.pow(a, b))


def ask_operation(stack, available_opt):
    keys = available_opt.keys()
    msg = ''
    while True:
        opt = input(msg + "[+|-|/|*|pow]:").strip()
        if not opt in keys:
            msg = 'please try again'
            continue
        stack.append(opt)
        break


def ask_number(stack):
    while True:
        x = input("Enter number:").strip()
        try:
            x = float(x)
            stack.append(x)
            break
        except ValueError as err:
            print("Please try again because we " + str(err))


def calculate(stack, available_opt):
    opt = stack.pop()
    func = available_opt[opt]
    func(stack)
    return stack.pop()


def main(exec_stack, available_opt):
    ask_number(exec_stack)
    ask_number(exec_stack)
    ask_operation(exec_stack, available_opt)
    answer = calculate(exec_stack, available_opt)
    print("Answer is", answer)


exec_stack = []


available_opt = {
    '+': opt_sum,
    '-': opt_minus,
    '/': opt_div,
    '*': opt_mult,
    'pow': opt_pow
}


main(exec_stack, available_opt)
