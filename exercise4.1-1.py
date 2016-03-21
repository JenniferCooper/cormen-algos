# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 10:20:08 2016

@author: jcoop
"""

"""
Implement both the bf and rec algo for the max-subarray prob. 
What prob size n0 gives the crossover point at which the rec algo
beats the bf algo?
Then, change the basecase of the rec algo to use the bf algo
whenever prob size is less than n0. Does that change the crossover point?
"""
import math
  
def maximumSubarrayBF(array, low, high):
    """
    brute force implementation of 'find max subarry' prob
    takes an array of positive and neg ints and low and high indices
    returns a triple of (left_index, right_index, max_sum)
    """
    max_sum = float("-inf")
    for i in range(len(array)):
        temp_sum = 0
        for j in array[i:]:
            temp_sum += j
            if temp_sum > max_sum:
                max_sum = temp_sum
                left_index = i
                right_index = array.index(j)
    return (left_index, right_index, max_sum)

#print "BF"
#test_array1 = [0, 1, -4, 3, -4]
#print maximumSubarrayBF(test_array1, 0, 3)
#test_array2 = [0, 13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
##(8, 11, 43)
#print maximumSubarrayBF(test_array2, 0, len(test_array2))

#i guess come up with a way to generate different n values?

def findMaxCrossingSubarray(array, low, mid, high):
    """
    takes array and indices low, mid, and high
    returns the tuple (left, right, sum)
    where left and right are the indices of the max crossing
    array, and sum is the product of the max crossing 
    array elements
    """
    left_index = 0
    left_sum = float("-inf")
    temp_sum = 0
    for i in range(mid-1, low-1, -1):
        temp_sum += array[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            left_index = i
    right_index = 0
    right_sum = float("-inf")
    temp_sum = 0
    for i in range(mid, (high + 1)):
        temp_sum += array[i]
        if temp_sum > right_sum:
            right_sum = temp_sum
            right_index = i
    return (left_index, right_index, left_sum + right_sum)

#print "Cross"
#cross_array = [-3, 2, 4, -1, 2, -4]
#print findMaxCrossingSubarray(cross_array, 0, 3, 5)
##(1, 4, 7)
#test_array1 = [0, 1, -4, 3, -4]
#print findMaxCrossingSubarray(test_array1, 0, 3, 4)
##(1, 3, 0)

def maximumSubarrayRec(array, low, high):
    """
    recursive implementation of FIND-MAXIMUM-SUBARRAY
    takes an array and the low and high indices and
    returns the maximum sum within the elements and their
    indices
    """
    #base case: only one element
    print "array",  array[low:high+1]
    print "low", low
    print "high", high
    if high == low or array == []:
        return (low, high, array[low])
    else:
        mid = (low+high)/2
        (left_low, left_high, left_sum) = maximumSubarrayRec(array, low, mid)
        print "left", (left_low, left_high, left_sum)
        (right_low, right_high, right_sum) = maximumSubarrayRec(array, mid+1, high)
        print "right", (right_low, right_high, right_sum)
        (cross_low, cross_high, cross_sum) = findMaxCrossingSubarray(array, low, mid, high)
        print "cross", (cross_low, cross_high, cross_sum)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

print
print "rec"
#print maximumSubarrayRec([3], 0, 0)
#print
#print maximumSubarrayRec([-3, 4], 0, 1)
#print
#test_array1 = [0, 1, -4, 3, -4]
#print maximumSubarrayRec(test_array1, 0, 4)
#TODO: find what was happening in cross in the above test
#(3, 3, 3)
#test_array2 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
#(8, 11, 43)
#print maximumSubarrayRec(test_array2, 0, 15)
test_array32 = [18, 20, -16, -23]
print maximumSubarrayRec(test_array32, 0, 3)
print
test_array23 = [-16, -23, 18, 20]
print maximumSubarrayRec(test_array23, 0, 3)
    
#testcases of different running times for n
#if __name__ == '__main__':
#    import timeit
#    print(timeit.timeit("maximumSubarrayBF()", setup="from __main__ import maximumSubarrayBF"))