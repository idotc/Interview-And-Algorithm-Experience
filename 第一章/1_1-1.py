import sys
def ReverseString(s, l1, l2):
    s = list(s)
    while(l1 < l2):
        t = s[l1]
        s[l1] = s[l2]
        s[l2] = t
        l1 = l1 + 1
        l2 = l2 - 1
    return s

def LeftRotateString(s, n, m):
    m = m %  n
    s = ReverseString(s, 0, m-1)
    s = ReverseString(s, m, n-1)
    s = ReverseString(s, 0, n-1)
    return s

def main():
    str = input("Enter your String:")
    m = int(input("Enter your shift number:"))
    n = len(str)
    str = LeftRotateString(str, n, m)
    str = ''.join(str)
    print(str)

if __name__=="__main__":
    sys.exit(main())