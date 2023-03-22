#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    count = len(sys.argv)
    if count != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    if op not in ["+", "-", "*", "/"]:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if op == "+":
        print(f"{a} {op} {b} = {add(a, b)}")
    elif op == "-":
        print(f"{a} {op} {b} = {sub(a, b)}")
    elif op == "*":
        print(f"{a} {op} {b} = {mul(a, b)}")
    else:
        print(f"{a} {op} {b} = {div(a, b)}")
