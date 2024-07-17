# Such Pair Returns

# Description

# For each test case, you are given N integers and K, your task is to write a program that prints "1" (without quotes) if there are 2 integers present in the array whose sum is K. Else pr int "-1" (without quotes).

# Given Input 


arr = [3, 4, 0, 2, 7]
k = 2
n = len(arr)



# output
# 1


def solve(arr, n, k):
    i = 0
    j = n-1
    arr.sort()
    ans  = "-1"
    
    while (i<j):
        if arr[i] + arr[j] == k:
            ans = "1"
            break
        elif arr[i] + arr[j] > k:
            j-=1
        else:
            i+=1
    return ans 



print(solve(arr, n, k))

