













listA = [200, 300, 700, 100, 150, 300,250,700, 750]

# Sorted list of numbers
listB =  [34,46,93,127,277,321,454,565,12201]


# Look for a number in sorted list
def orderedLinearSearch(listB, number):
    for i in range(len(listA)):
        if listB[i] == number:
            return i
        elif listB[i] > number:
            return -1
    return -1

##############################################################################################
# Given an array of n numbers, give an algorithm for checking whether there are any
# duplicate elements in the array or no?
duplicatelist = [1,2,2,3,4]

#1.bruteforce method
def duplicateexist(A):
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)-1):
            if A[i] == A[j]:
                print("Duplicate exists!")
                return True
    return False
# complexity : O(n2)

# 2.Using sorting
def duplicateexist_sorting(A):
    A.sort()
    for i in range(0, len(A)-2):
        if A[i] == A[i+1]:
            print("Duplicate exist!")
            return True
    print("No Duplicate!")
    return False
# Complexity : O(n logn) + O( n )


# 3. Hashing - O(n) and O(n)

# 4.Negation technique
import math
def CheckDuplicatesNegationTechnique(A):
    for i in range(0, len(A)):
        if A[abs(A[i])] < 0:
            print("Duplicates exist:", A[i])
            return
        else:
            A[abs(A[i])] *= -1

    print("No duplicates in given array.")
# Notes:
# This solution does not work if the given array is read only.
# This solution will work only iJ all the array clements are positive.
# If the elements range is not in O to n - l the n it may give exceptions.

# Note: Query questions
# 1.What is the range of input values?
# 2.Are all the numbers are positive ?
# 3.Is the input array or list is immutable?

print(duplicateexist(duplicatelist))
print(duplicateexist_sorting(duplicatelist))

##############################################################################################
# Brute forece
def MaxRepititionsBruteForce(A):
    n = len(A)
    count = max = 0
    for i in range(0, n):
        count = 1
        for j in range(0, n):
            if i != j and A[i] == A[j]:
                count += 1
        if max < count:
            max = count
            maxRepeatedElement = A[i]
    print(maxRepeatedElement, "repeated for ", max)


# Using hash
def MaxRepititionsWithHash(A):
    A_dict = {}
    max = 0
    maxRepeatedElement = 0

    for elem in A:
        if elem in A_dict:
            A_dict[elem] = A_dict[elem] + 1
        else:
            A_dict[elem] = 1

    for element in A:
        if A_dict[element] > max:
            max = A_dict[element]
            maxRepeatedElement = element
    print("Using hash algo:" , maxRepeatedElement, "repeated for ", max)
    return (maxRepeatedElement,max)

A = [3, 2, 1, 2, 2, 3, 2, 1, 3]
MaxRepititionsWithHash(A)

#######################################################################

# Using hash
# complexity: O(n), O(n) space and time
def FirstRepeatedElementAmongRepeatedElementsWithhash(A):
    table = {}

    for element in A:
        if element in table:
            table[element] = table[element] + 1
        else:
            table[element] = 1

    for elem in A:
        if table[elem] > 1:
            print(" First repeated element in array:", elem)
            return elem

A = [3,2,1,1,2,1,2,5,3,5]
FirstRepeatedElementAmongRepeatedElementsWithhash(A)
#######################################################################
# Finding the Missing Number: We are given a list of n - 1 integers and these integers
# are in the range of I to 11. There arc no duplicates in the list. One of the integers
# is missing in the list. Given an algorithm to find the missing integer.
# Example: 1/P: I l.2,4.6,3, 7,81 O/P: 5

def findMissingNumber(A):
    sum = 0
    for elem in A:
        sum = sum + elem

    nooflelements = len(A) + 1
    nelements_sum = (nooflelements * (nooflelements + 1 )) / 2
    print("Missing Number: ", nelements_sum - sum )
    return nelements_sum - sum

A = [1,2,3,4,6,7,8,9,10]
print(findMissingNumber(A))

# Note: if the sum or the numbers goes beyond the maximum allowed integer, then there
#       can be integer overflow and we may not get the correct answer.

def findMissingNumber_xor(A):
    X = 0

    # XOR over the range of numbers
    for i in range(1, len(A)+ 2):
        X = X ^ i

    for i in range(0,len(A)):
        X = X ^ A[i]

    print("Missing Number [with XOR]: ", X)
    return X

A = [1,2,3,4,6,7,8,9,10]
print(findMissingNumber_xor(A))
#######################################################################
#Given an array of n lements. Find two elements in the array such
# that their sum is equal to given element K.

A = [1, 4, 45, 6, -81, 10, -82]

def twoElementsWithSumKWithHash(A, k):
    table = {}
    for i in range(0,len(A)):
        table[A[i]] = i

    for elem in A:
        if k-elem in table:
            print(" the 2 elements are ", elem, k-elem)
            print("the indices of elements are ", table[elem], table[k-elem])
            break

# Note::
# display message if sum is not possible
# check if the numbers are integers or not

def twoElementswithsumk(A,k):
    A.sort()
    low  = 0
    high = len(A) - 1

    while low < high:
        if A[low] + A[high] == k:
            return 1
        elif A[low] + A[high] < k:
            low = low + 1
        else:
            high = high - 1
    return 0

#complexity: O(n logn )

print(" sum of 2 numbers : -71 exist in " , twoElementswithsumk(A,-71))
twoElementsWithSumKWithHash(A,-71)


#######################################################################

#sort the array
# initialize 2 sums - positive closest : 0 and negative closest : 0
# start 2 indices : one from beginning and other from end
# if sum > 0 and < positive closest


import sys
def TwoElementsClosestToZero(A):
    positive_sum = sys.maxsize
    A.sort()
    n = len(A)
    low = 0
    high = n-1
    minright = minleft = 0
    while low < high:
        sum = A[low] + A[high]
        if abs(sum) < positive_sum:
            positive_sum = sum
            minleft = low
            minright = high
        elif sum > 0 and sum < positive_sum:
            high = high -1
        else:
            low = low + 1
    print(" the two elements which are closest to zero are ", A[minleft] , " and ", A[minright])



A = [1, 60, - 10, 70, -80, 85]
TwoElementsClosestToZero(A)

A=[10,8,3,5,-9,-7,6]
TwoElementsClosestToZero(A)

#####################################################################

# if mid > mid +1, return mid
# if mid -1 > mid return mid - 1
# initialize low and high - take the midpoint


def findMinimumlnRotatedSortedArray(A):
    length = len(A) - 1
    low = 0
    high = length
    pivot = findPivot(A,low,high)
    return pivot


def findPivot(A,low,high):
    if low > high:
        return -1

    if low == high:
        return low

    while low < high:
        mid = (low + high) // 2
        if (mid < high) and (A[mid] > A[mid + 1]):
            return mid

        if mid > low and A[mid-1] > A[mid]:
            return mid-1

        if A[low] >= A[mid]:
            return findPivot(A,low, mid-1)
        else:
            return findPivot(A,mid+1, high)


A= [15, 16, 19, 20, 25, 27,29, 33, 1, 3, 4 , 5, 7, 10, 14,17,19]
B= [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
print("the index :")
print(findMinimumlnRotatedSortedArray(A))
print(findMinimumlnRotatedSortedArray(B))

#####################################################################

#Problems : 46 and 47 - revise the conditions

#array with duplicates - find first occurence

A = [1,2,2,2,3,4]
# find first occurence of 2 :
# low == mid and A[mid] == data || data > A[mid-1] and A[mid] == data

# find last occurence of 2:
# mid == high and A[mid] == data || A[mid] == data and A[mid+1] > A[mid}

def binarySearchFirstOccurrence(A, target):
    if A == None or len(A) == 0:
        return -1
    high = len(A) - 1
    low = 0
    m = 0
    lastFound = -1
    while 1:
        if low > high:
            return lastFound

        m = (low + high) // 2

        if A[m] == target:
            lastFound = m
            high = m - 1

        if A[m] < target:
            low = m + 1
        if A[m] > target:
            high = m - 1

    return m


A = [5, 6, 9, 12, 15, 21, 21, 34, 45, 57, 70, 84]
print("Find First occurence of a number in array!!")
print("last occurence:", binarySearchFirstOccurrence(A,21))


def binarySearchLastOccurrence1(A,data):
    if len(A) == 0:
        print("Array is empty!")
        return -1

    low = 0
    m = 0
    high = len(A)-1

    while low < high:
        mid = (low + high ) // 2

        if A[mid] == data and mid == high:
            return mid

        if A[mid] == data and A[mid+1] > A[mid]:
            return mid

        if A[mid] > data:
            high = mid - 1

        if A[mid] < data:
            low = mid + 1

# mid == high && A[mid] == data || A[mid] = data && A[mid + 1] > data

def binarySearchLastOccurrence(A, target):
    if len(A) == 0:
        return -1

    high = len(A) - 1
    low = 0
    m = 0
    lastFound = -1
    while 1:
        if low > high:
            return lastFound

        m = (low + high) // 2

        if A[m] == target:
            lastFound = m
            low = m + 1

        if A[m] < target:
            low = m + 1

        if A[m] > target:
            high = m - 1

    return m

A = [5, 6, 9, 12, 15, 21, 21, 34, 45, 57,70, 84]
#A = [5, 6, 9, 12, 15, 21, 21]
print("Find last occurence of a number in array!!")
print("last occurence:", binarySearchLastOccurrence(A,21))

#########################################################################



