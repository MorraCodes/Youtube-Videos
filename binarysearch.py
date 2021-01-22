"""
Created on Thu Jan 21 21:29:15 2021
@author: Omar M.H , on MorraCodes YT channel


[start,.............MIDDLE..Target.........,end]
       
         target is Greater than Middle OR Middle
            
[start,...Target...MIDDLE...,end]

        target is SMALLER than Middle OR Middle
[start,.Target..MIDDLE.,end]
.
.
.
.
.
.
.
.
until THE MIDDLE IS EQUAL TO THE TARGET.  

BigO(log(n))            

"""
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,100,200,300,500,6000,77777]

def binary_search(array, target):
	# length of the array
	n = len(array) 
	
	# variables.
	start = 0
	end = n - 1
	
	while start <= end:
		guess = (start + end) // 2
		if array[guess] == target:
			return guess
		elif  target < array[guess]: 
			end = guess - 1
		elif  target > array[guess]:
			start = guess + 1
	return -1
		






target = 300
location = binary_search(array, target)

print()
print(f"The index of the target:{target} is at index:{location}")


target = 11
location = binary_search(array, target)
print()
print(f"The index of the target:{target} is at index:{location}")
