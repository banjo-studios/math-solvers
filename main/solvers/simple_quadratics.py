import sys


def main():
    args = sys.argv
    args.pop(0)

    for _ in args:
        try:
            args[args.index(_)] = int(_)
        except ValueError:
            print(f"Invalid value '{_}' which is an integer")
            exit()

    if len(args) <= 2:
        print("No values/less than 3 were inputted")
        exit()

    print(f"Input:\n(ax²+bx+c): {args[0]}x²+{args[1]}x+{args[2]}")
    if args[0] == 1: #If simple quadratic
        pass


if __name__ == "__main__":
    main()
