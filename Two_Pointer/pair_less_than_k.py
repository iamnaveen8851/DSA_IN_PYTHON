# Pair less than K

# Description

# You are given an array A of N integers, and an integer K. Find the maximum value of S, such S that S = a[i] + a[j], and S < K. If no such value exists, then print -1.
# Refer the sample test case for better understanding.

# input 1

arr1 = [1, 2, 3, 4, 5]
n1 = len(arr1)
k1 = 7
# input 2

arr2 = [30, 10, 20]
n2 = len(arr2)
k2 = 15


def solve(arr, n, k):
    arr.sort()
    i = 0
    j = n-1
    sumArr = []
    while(i < j):
        s = arr[i] + arr[j]
        if s < k:
            sumArr.append(s)
            i+=1
        else:
            j-=1
    
    if len(sumArr) > 0:
        return (max(sumArr))
    else:
        return (-1)


print(solve(arr2, n2, k2))