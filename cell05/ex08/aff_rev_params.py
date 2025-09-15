"""Display an Array in Reverse Order"""
import sys

def main():
    """Display an Array in Reverse Order"""
    if len(sys.argv) > 2:
        print('\n'.join(reversed(sys.argv[1:])))
    else:
        print("none")


main()
