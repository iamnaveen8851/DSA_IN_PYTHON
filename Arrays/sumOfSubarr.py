# Description
# You are given an array of N integers and a single integer K. You need to find out if there is a subarray, which has the sum exactly as K.

# input 
# 3
# 5 3
# 1 2 1 3 4
# k = 5
# arr = [1, 2, 1, 3]
# n = len(arr)


# arr = [1, 2, 1]
# k = 2
n = len(arr)

# steps
#   - find the subarr first
#   - sum of subArr
# check sum == k return "YES" else return "NO"

def solve(arr, n, k):
    for i in range(n):
        for j in range(n):
            sum_ = sum(arr[i:j+1])
            if sum_ == k:
                 print("YES")
                 return
    print("NO")
    return
    
solve(arr, n, k)
