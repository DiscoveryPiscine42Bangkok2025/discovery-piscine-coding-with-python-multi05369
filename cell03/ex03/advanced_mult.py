"""return multiplication table"""

def main():
    """print multiplication tables from 0 to 10 using while loops"""
    number = 0
    while number <= 10:
        print(f"Table de {number}:", end=" ")
        multiply = 0
        while multiply <= 10:
            end_char = "\n" if multiply == 10 else " "
            print(number * multiply, end=end_char)
            multiply += 1
        number += 1


main()
