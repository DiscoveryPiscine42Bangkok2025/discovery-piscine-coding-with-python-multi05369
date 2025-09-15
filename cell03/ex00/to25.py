"""Print number to 25"""

def main():
    """Print number to 25"""
    number = int(input("Enter a number less than 25 "))
    if number > 25:
        print("Error")
        return
    for i in range(number, 26):
        print(f"Inside the loop, my variable is {i}")


main()
