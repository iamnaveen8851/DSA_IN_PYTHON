s  ="abcdef"
n = len(s)


#stage1 . substring
#stage2 check length of substring is prime number or not and count it 
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def subString(s, n):
    count = 0
    for i in range(n):
        for j in range(n):
            subStr_  = s[i:j+1]
            print(subStr_)
            if(isPrime(len(subStr_))):
                count+=1
    print(count)

subString(s, n)

