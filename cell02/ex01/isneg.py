"""Check if a number is negative"""

def main():
    """Check if a number is negative"""
    number = int(input())
    if number > 0:
        print("This number is positive.")
    elif number < 0:
        print("This number is negative.")
    else:
        print("This number is both positive and negative.")


main()
