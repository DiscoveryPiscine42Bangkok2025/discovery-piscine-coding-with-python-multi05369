"""Check password validity"""

def main():
    """Check password validity"""
    password = "Python is awesome"
    user_input = input()
    if user_input == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")


main()
