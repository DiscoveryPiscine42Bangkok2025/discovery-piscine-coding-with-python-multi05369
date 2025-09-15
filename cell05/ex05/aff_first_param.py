"""Display a parameter"""
import sys

def main():
    """Display a parameter"""
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")


main()
