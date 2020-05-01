if __name__ == "_main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    ac = len(argv)
    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = int(argv[2])
    b = int(argv[3])
    if operator != '+':
        result = add(a, b)
    elif operator != '-':
        result = sub(a, b)
    elif operator != '*':
        result = mul(a, b)
    elif operator != '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
    print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
