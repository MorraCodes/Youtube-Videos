"""
Created on Thu Jan 28 18:28:46 2021
@author: MorraCodes
"""

array = [9,5,3,2,1,100,55,22,11,10] # this unsorted array

def bubble_sort(array):
    isSorted = False # unsorted array boolean
    
    while not isSorted: # as long as it is not sorted keep going / sorting
        isSorted = True # sorted
        loop_less = 0
        for i in range(len(array) - 1 - loop_less):
            if array[i] >  array[i+1]:
                array[i], array[i+1] = array[i+1],array[i] # swap procedure
                isSorted = False # unsorted
            loop_less += 1
    return array
                
                
            

sorted_array = bubble_sort(array) # sorted array
print(sorted_array)
