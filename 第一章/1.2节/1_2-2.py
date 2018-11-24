import sys

def StringContain(a, b):
    a = list(a)
    b = list(b)
    a = sorted(a)
    b = sorted(b)
    pa = 0
    pb = 0
    while (pb < len(b)):
        while((pa < len(a)) & (a[pa] < b[pb])):
            pa = pa + 1
        if((pa >= len(a)) | (a[pa] >b[pb])):
            return False
        pb = pb + 1
    return True

def main():
    stra = input("Enter string a :")
    strb = input("Enter string b :")
    result = StringContain(stra, strb)
    print ("The result is :"+ str(result))

if __name__ == "__main__":
    sys.exit(main())