# Dhoni Fan

# Description

# Alex is a huge Dhoni Fan, so naturally he loves the number 7. He has an array of size N, so he wants to find all the subarrays which contain the number 7 atleast once. Help him, fin d all such subarrays.


# Given Input 

arr = [1, 2, 7]
n = len(arr)

# approach 
# create subarr 
# check subarr should contain the number 7 or not 
# count it 

def findSubArr(arr, n):
    count = 0
    for i in range(n):
        for j in range(n):
            subArr = arr[i:j+1]
            if 7 in subArr:
                count+=1
    print(count)

findSubArr(arr, n)