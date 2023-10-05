#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argcont = len(sys.argv) - 1
    if argcont == 1:
        print("1 argument", end="")
    else:
        print("{} arguments".format(argcont), end="")
    if argcont > 0:
        print(":", end="")
    else:
        print(".", end="")

    print()
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
