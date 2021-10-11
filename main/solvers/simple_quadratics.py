import sys
from utils.sqrt import sqrt
from utils.fabs import fabs


def main():
    args = sys.argv
    args.pop(0)

    for _ in args:
        try:
            args[args.index(_)] = int(_)
        except ValueError:
            print(f"Invalid value '{_}' which is not an integer")
            exit()

    if len(args) < 3:
        print("No values/less than 3 were inputted")
        exit()
    elif len(args) > 3:
        print("More than 3 values were inputted")
        exit()

    a = args[0]
    b = args[1]
    c = args[2]

    equation = ""
    if a == 1:
        a_display = "x²"
    elif a == 0:
        print("x² value cannot be zero!")
        exit()
    elif a == -1:
        a_display = "-x²"
    else:
        a_display = str(a) + "x²"
    equation += (a_display + "+")

    if b == 1:
        b_display = "x"
        equation += b_display
    elif b == 0:
        b_display = ""
    elif b == -1:
        b_display = "-x"
        equation += b_display
    else:
        b_display = str(b) + "x"
        equation += (b_display + "+")
    equation += str(c)

    output = f"Input:\n(ax²+bx+c): {equation}"
    output = output.replace("+-", "-")
    output = output.replace("--", "+")
    output = output.replace("-+", "-")
    print(output)

    if args[0] == 1:
        factors = [(i, int(c / i)) for i in range(1, int(sqrt(fabs(c))) + 1) if c % i == 0]
        print(f"Find factor pairs of c:\n{factors}")

    # See if any factor pairs can match up to make centre value


if __name__ == "__main__":
    main()
