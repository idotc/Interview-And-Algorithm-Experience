import sys

def ReverseWord(s, to):
    start = 0
    while(start < to):
        t = s[start]
        s[start] = s[to]
        s[to] = t
        start = start + 1
        to = to - 1
    return s

def LeftRotateWord(s):
    s = s.split(" ")
    n = len(s)
    s = ReverseWord(s, n-1)
    str = []
    for i in range(2*n-1):
        if(i % 2 == 0):
            str.append(s[int(i/2)])
        else:
            str.append(" ")
    str = ''.join(str)
    return str

def main():
    str = input("Enter a sentence:")
    n = len(str)
    str = LeftRotateWord(str)
    print (str)

if __name__ == "__main__":
    sys.exit(main())
