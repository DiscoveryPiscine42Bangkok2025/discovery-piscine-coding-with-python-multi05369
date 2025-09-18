import sys
from checkmate import checkmate

def main():
    """
    Main function to read board from stdin and check for checkmate.
    """
    try:
        board = []
        for line in sys.stdin:
            line = line.rstrip('\n')
            if line:
                board.append(list(line))
        
        if checkmate(board):
            print("Success")
        else:
            print("Fail")
            
    except Exception:
        print("Fail")

if __name__ == "__main__":
    main()
    