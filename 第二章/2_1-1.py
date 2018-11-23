import sys
def StringContain(a, b):
    a = list(a)
    b = list(b)
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if(b[j] != a[i]):
                count = count + 1
        if (count == len(b)):
            return False
    return True


def main():
    stra = input("Enter string a:")
    strb = input("Enter string b:")
    result = StringContain(stra, strb)
    print ("The result is : "+str(result))

if __name__ == "__main__":
    sys.exit(main())