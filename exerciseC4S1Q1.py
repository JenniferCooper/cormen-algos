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
import helpers
import time


class MaxSubarrayImplementations:
  
    def maximumSubarrayBF(self, array, low, high):
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

    #i guess come up with a way to generate different n values?

    def findMaxCrossingSubarray(self, array, low, mid, high):
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

    def maximumSubarrayRec(self, array, low, high):
        """
        recursive implementation of FIND-MAXIMUM-SUBARRAY
        takes an array and the low and high indices and
        returns the maximum sum within the elements and their
        indices
        """
        #base case: only one element
        #print "array",  array[low:high+1]
        #print "low", low
        #print "high", high
        if high == low or array == []:
            return (low, high, array[low])
        else:
            obj = MaxSubarrayImplementations()
            mid = (low+high)/2
            (left_low, left_high, left_sum) = obj.maximumSubarrayRec(array, low, mid)
           # print "left", (left_low, left_high, left_sum)
            (right_low, right_high, right_sum) = obj.maximumSubarrayRec(array, mid+1, high)
         #   print "right", (right_low, right_high, right_sum)
            (cross_low, cross_high, cross_sum) = obj.findMaxCrossingSubarray(array, low, mid, high)
           # print "cross", (cross_low, cross_high, cross_sum)
            if left_sum >= right_sum and left_sum >= cross_sum:
                return (left_low, left_high, left_sum)
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return (right_low, right_high, right_sum)
            else:
                return (cross_low, cross_high, cross_sum)


#generate increasing large num of arrays, then time running time for each algo
def runTimeComparison(num):
    #generate arrays
    array_of_arrays = []
    bF_array = []
    rec_array = []
    for ea in range(1, num+1):
        array_of_arrays.append(helpers.arrayGenerator(ea))
    #run both BF and Rec methods on each array
    maxObj = MaxSubarrayImplementations()
    for array in array_of_arrays:
        start_time = time.clock()
        maxObj.maximumSubarrayBF(array, 0, (len(array) -1))
        meth_time = (time.clock() - start_time)
        bF_array.append(meth_time)
        start_time = time.clock()
        maxObj.maximumSubarrayRec(array, 0, (len(array) -1))
        meth_time = (time.clock() - start_time)
        rec_array.append(meth_time)
    return bF_array
    
import matplotlib.pyplot as plt

def plotTimes():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_points = xrange(0,9)
    y_points = xrange(0,9)
    p = ax.plot(x_points, y_points, 'b')
    ax.set_xlabel('x-points')
    ax.set_ylabel('y-points')
    ax.set_title('Simple XY point plot')
    fig.show()

start_time = time.time()
print "starting"
#print runTimeComparison(50)
#plotTimes()
fig = plt.figure()
ax = fig.add_subplot(111)
x_points = xrange(0,9)
y_points = xrange(0,9)
p = ax.plot(x_points, y_points, 'b')
ax.set_xlabel('x-points')
ax.set_ylabel('y-points')
ax.set_title('Simple XY point plot')
fig.show()
print("--- %s seconds ---" % (time.time() - start_time))