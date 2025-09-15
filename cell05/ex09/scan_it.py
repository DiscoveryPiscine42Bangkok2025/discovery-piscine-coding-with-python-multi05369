"""Scanning a Text"""
import sys

def main():
    """Scanning a Text"""
    if len(sys.argv) != 3:
        print("none")
        return
    keyword = sys.argv[1]
    text = sys.argv[2]
    found = text.count(keyword)
    print(found)


main()
