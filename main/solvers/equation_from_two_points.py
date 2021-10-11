import sys


def main():
    args = sys.argv
    args.pop(0)

    for _ in args:
        try:
            args[args.index(_)] = int(_)
        except ValueError:
            raise ValueError(f"Invalid value '{_}' which is not an integer")

    if len(args) == 0:
        raise ValueError("No inputted values")

    m = (args[3] - args[1]) / (args[2] - args[0])
    print(f"Gradient:\n((y2-y1)/(x2-x1)): ({args[3]}-{args[1]})/({args[2]}-{args[0]}) = {m}")
    c = (-(m * args[0])) + args[1]
    print(
        f"Find Y-intercept:\n(y=mx+c): {args[1]}={m}x+c\n(c=-mx+y): c=-{m}x+{args[1]}\n(c=-mx+y): c=-({m}x{args[0]})+{args[1]}=-{m * args[0]}+{args[1]}={c}")
    output = f"(y=mx+c): y={m}x+{c}"
    output = output.replace("+-", "-")
    output = output.replace("--", "+")
    output = output.replace("-+", "-")
    print("Solutions:")
    print(output)
    other_format_x = (args[1] - args[3])
    other_format_y = (args[2] - args[0])
    other_format_c = (args[0] * args[3]) - (args[2] * args[1])
    output = f"(ax+bx+c=0): {other_format_x}x+{other_format_y}y+{other_format_c}=0"
    output = output.replace("+-", "-")
    output = output.replace("--", "+")
    output = output.replace("-+", "-")
    print(output)


if __name__ == "__main__":
    main()
