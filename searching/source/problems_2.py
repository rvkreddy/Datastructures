# Separate even and odd numbers: Given an a rray Al]. write a function that segregates
# even and odd numbers. The functions s hould put a ll even numbers first, and then
# odd numbers.

# Assumptions:
#1.Mutable
#2.numbers are +ve
#3.


def separateEvenOdd(A):

    if len(A) == 0:
        print("Empty Array")

    low = 0
    high = len(A) - 1

    while low < high:
        if A[low] % 2 != 0 and A[high] % 2 == 0:
            temp = A[low]
            A[low] = A[high]
            A[high] = temp
            low += 1
            high -= 1
            continue

        if A[low] % 2 == 0:
            low += 1

        if A[high] % 2 != 0:
            high -= 1


A= [12, 34, 45, 9, 8, 90, 3, 4,5, 3,3,3,3,4,3,3,4,4,4]
print(A)
separateEvenOdd(A)
print(A)
################################################################


def separateonesandzeros(A):
    if len(A) == 0:
        print("Empty Array")

    low = 0
    high = len(A) - 1

    while low < high:
        if A[low] == 1 and A[high] == 0:
            temp = A[low]
            A[low] = A[high]
            A[high] = temp
            low += 1
            high -= 1
            continue

        if A[low] == 0:
            low += 1

        if A[high] == 1:
            high -= 1



A= [1,0,0,0,1,0,1,1,1,0,0,0,1]
print(A)
separateonesandzeros(A)
print(A)

################################################################
# Sort an array of O's, l's and 2's [or R's, G's and B's): Given a n array
# All consisting of O's, l's and 2's, give a n a lgorithm for sorting.
# The Algorithm should put all O's first, then all l's and finally all 2's at the end.
#https://www.youtube.com/watch?v=sEQk8xgjx64

def seperate012(A):

    if len(A) == 0:
        print("empyt input array")

    l = m = 0
    h = len(A)-1

    while m <= h:
        if A[m] == 0 and m <= h:
            temp = A[m]
            A[m] = A[l]
            A[l] = temp
            m += 1
            l += 1

        if A[m] == 1 and m <= h:
            m += 1

        if A[m] == 2 and m <= h:
            # Note: remember, last element can be 2 already, so don't increment m after swapping
            temp = A[m]
            A[m] = A[h]
            A[h] = temp
            h -= 1

A = [0,1,2,0,1,2,0,1,2]
print(A)
seperate012(A)
print(A)

##################################################################

def numberOfTrailingZeros(n):
    if n<0:
        return -1

    count = 0
    i = 5
    while n//i > 0:
        count = count + n//i
        i = i * 5
    return count

print(numberOfTrailingZeros(25))
#Time Complexity: 0(logn).

##################################################################







