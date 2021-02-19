"""
Created on Thu Jan 28 18:28:46 2021

@author: omarm
"""

array = [10, 7, 9, 5, 8, 6] # this unsorted array


# BigO(n**2)         
def insertionSort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j] , array[j-1] =  array[j-1], array[j]
            j -= 1
    return array             
            

sorted_array = insertionSort(array) # sorted array
print(sorted_array)
