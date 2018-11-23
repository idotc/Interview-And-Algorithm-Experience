import sys

def StringContain(a, b):
    hash = 0
    for i in range(len(a)):
        hash = hash | (1 << (ord(a[i])-ord('A')))
    for i in range(len(b)):
        if( (hash & (1 << (ord(b[i])-ord('A')))) == 0 ):
            return False
    return True

def main():
    stra = input("Enter string a :")
    strb = input("Enter string b :")
    result = StringContain(stra, strb)
    print ("The result is :"+ str(result))

if __name__ == "__main__":
    sys.exit(main())