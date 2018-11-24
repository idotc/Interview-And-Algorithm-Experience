import sys

def StringContain(a, b):
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
         59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    f = 1
    for i in range(len(a)):
        x = p[ord(a[i]) - ord('A')]
        if (f % x):  ## 同样的字符对应的素数不要重复乘，防止增加无效的数据量
            f = f * x
    for i in range(len(b)):
        x = p[ord(b[i]) - ord('A')]
        if(f % x):
            return False
    return True

def main():
    print (int(ord('B')-ord('A')))
    stra = input("Enter string a :")
    strb = input("Enter string b :")
    result = StringContain(stra, strb)
    print ("The result is :"+ str(result))

if __name__ == "__main__":
    sys.exit(main())
