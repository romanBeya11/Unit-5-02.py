'''
Created by Roman Beya
Created on 15-11-17
Created for ICS3U
This program returns the largest number stored in an array
'''
def array_function(array = []):
	# This function will loop through the array parameter, looking for the largest number
	for i in range(len(array)):
		Max = max(array)
	return Max

array = [2, 4, 87, 2918, 3948]
max_num_in_array = array_function(array)
print max_num_in_array
