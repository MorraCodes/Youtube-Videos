"""
Created on Tue Jan 26 19:43:50 2021

@author: omarm
"""

array = [9,5,3,2,1,100,55,22,11,10]


def bubble_sort(array):
    isSorted = False
    loop_less = 0
    while not isSorted:
        isSorted = True
        for i in range( len(array) - 1 - loop_less):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1] , array[i]
                isSorted = False
        loop_less += 1
    return array
                

sorted_array = bubble_sort(array)
print(sorted_array)
