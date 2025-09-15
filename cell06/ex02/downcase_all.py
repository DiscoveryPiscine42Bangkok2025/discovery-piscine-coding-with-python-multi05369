"""Let’s Stroll in the Array"""
import sys

def downcase_all(arr):
    """Convert all strings in an array to lowercase"""
    return [s.lower() for s in arr]


print(*downcase_all(sys.argv[1:]), sep="\n")
