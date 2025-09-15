"""Print multiplication table"""

def main():
    """Print multiplication table"""
    number = int(input("Enter a number\n"))
    for i in range(10):
        print(f"{i} x {number} = {number * i}")


main()

