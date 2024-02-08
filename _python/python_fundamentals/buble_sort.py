test_list = [1,2,3,4,5,6,8,7]

def bubble_sort(input_list):
	for i in range(len(input_list)):
		#swapped varialbe keeps track if any swapping occured in the second loop. if no swapps occured then the array is sorted hence no need to keep the parent loop
		swapped = False
		print("Loop number:",i,"/",len(input_list)-1)
		for idx in range(len(input_list) - i - 1):
			if input_list[idx] > input_list[idx + 1]:
				input_list[idx], input_list[idx + 1] = input_list[idx + 1], input_list[idx]
				swapped = True
		if not swapped:
			break
	return input_list

print(bubble_sort(test_list))
