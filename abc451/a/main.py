import sys
from collections import deque, Counter

def main():
    s = input()
    n = len(s)
    if n % 5 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()