"""Understanding Strings as Arrays"""
import sys

def main():
    """Understanding Strings as Arrays"""
    if len(sys.argv) == 2:
        string = sys.argv[1]
        countz = string.count('z')
        if countz == 0:
            print("none")
        else:
            print("z" * countz)
    else:
        print("none")


main()
