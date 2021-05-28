#Leetcode 41
#a, b = b, a

def solution(A):
    
    def swap(nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]

    for i in range(len(A)):
        while 1 <= A[i] <= len(A) and A[i] != A[A[i]-1]:
            swap(A, i, A[i]-1)

    for i in range(len(A)):
        if i != A[i] -1: 
            return i + 1
    return len(A)+1