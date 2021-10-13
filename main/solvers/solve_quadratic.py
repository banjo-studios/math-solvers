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

    if a == 1:
        a_display = "x²"
    elif a == -1:
        a_display = "-x²"
    elif a == 0:
        print("a value cannot be 0")
        exit()
    else:
        a_display = str(a) + "x²"

    if b == 1:
        b_display = "x"
    elif b == -1:
        b_display = "-x"
    elif b == 0:
        b_display = str(b)
    else:
        b_display = str(b) + "x"


    output = f"Input:\n{a_display}+{b_display}+{c}"
    output = output.replace("+-", "-")
    output = output.replace("--", "+")
    output = output.replace("-+", "-")
    print(output)

    b_squared = b ** 2
    four_a_c = 4 * a * c
    if b_squared - four_a_c < 0:
        __ = (b_squared - four_a_c) - ((b_squared - four_a_c) * 2)
    else:
        __ = (b_squared - four_a_c)

    top_sqrt = sqrt(__)

    top_pos = (-b) + top_sqrt
    top_neg = (-b) - top_sqrt
    two_a = 2 * a
    output = f"Substitution:\n(-{b}+sqrt({b}^2-4({a})({c}))/2({a})"
    output = output.replace("+-", "-")
    output = output.replace("--", "+")
    output = output.replace("-+", "-")
    print(output)

    print("Roots:\n" + str((top_pos/two_a)) + ", " + str(top_neg/two_a))


if __name__ == "__main__":
    main()
