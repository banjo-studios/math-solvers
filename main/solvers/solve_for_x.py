import sys

def main():
    args = sys.argv
    args.pop(0)

    for _ in args:
        try:
            args[args.index(_)] = int(_)
        except ValueError:
            print(f"Invalid value '{_}' which is not an integer")
            exit()

    if len(args) < 2:
        print("No values/less than 2 were inputted")
        exit()
    elif len(args) > 2:
        print("More than 2 values were inputted")
        exit()

    a = args[0]
    b = args[1]

    if a == 1:
        a_display = "x"
    elif a == -1:
        a_display = "-x"
    elif a == 0:
        print("a value cannot be 0")
        exit()
    else:
        a_display = str(a) + "x"

    if b == 1:
        b_display = 1

    if b == -1:
        b_display = -1
    else:
        b_display = str(b)