"""Identifying a Parameter"""
import sys

def main():
    """Identifying a Parameter"""
    if len(sys.argv) == 1:
        print("none")
    else:
        param = sys.argv[1]
        check = input("What was the parameter? ")
        if param == check:
            print("Good job!")
        else:
            print("Nope, sorry...")


main()
