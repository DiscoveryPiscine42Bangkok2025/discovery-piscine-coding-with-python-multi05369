"""check float number"""

def main():
    """check float number"""
    number = float(input("Give me a number: "))
    if number.is_integer() and int(number):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")


main()
