import sys

def LeftShiftOne(str, n):
    s = []
    s = list(str)
    t = s[0]
    for i in range(1,n):
        s[i-1] = s[i]
    s[n-1] = t
    return s


def LeftRotateString(s, n, m):
    while(m):
        s = LeftShiftOne(s, n)
        m = m - 1
    return s


def main():
    str = input("Enter your input: ")
    m = int(input("Enter your shift numbers: "))
    len1 = len(str)
    str = LeftRotateString(str, len1, m)
    str = ''.join(str)
    print (str)

if __name__ == "__main__":
    sys.exit(main())