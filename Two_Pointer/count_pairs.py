# Count such pairs

# Description

# You are given an array A of N integers along with a target integer K.
# Your task is to find out the number of pairs of integers present in the array, whose sum is equal to the target value K.


# Input 

arr = [3, 0, 6, 2, 7]
n = len(arr)
k = 9

# output - 2

def count_pairs(arr,n, k):
    i = 0
    j = n-1
    arr.sort()
    count = 0
    while (i < j):
        if arr[i] + arr[j]  == k:
            count+=1
            i+=1
            j-=1
        elif arr[i] + arr[j] > k:
            j-=1
        else:
            i+=1
    return count


print(count_pairs(arr,n, k))
