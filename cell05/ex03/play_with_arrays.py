"""Manipulating Arrays, Still!"""

def main():
    """Manipulating Arrays, Still!"""
    arr = [2, 8, 9, 48, 8, 22, -12, 2]
    new_arr = [x + 2 for x in arr]
    new_new_arr = []
    for i in new_arr:
        if i > 5:
            new_new_arr.append(i)
    print(set(new_new_arr))


main()
