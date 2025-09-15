"""Methods Everywhere!"""
import sys

def shrink(text=""):
    """display first eight characters of text"""
    if isinstance(text, str):
        print(text[:8])


def enlarge(text=""):
    """append Z to text until it is 8 characters long"""
    if isinstance(text, str):
        while len(text) < 8:
            text += "Z"
        print(text)


if len(sys.argv) == 1:
    print("none")
else:
    for arr in sys.argv[1:]:
        if len(arr) < 8:
            enlarge(arr)
        elif len(arr) > 8:
            shrink(arr)
        else:
            print(arr)
