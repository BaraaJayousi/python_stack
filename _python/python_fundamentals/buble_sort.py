test_list = [2,5,1,3,6,8,4,7]

def bubble_sort(input_list):
	for i in range(len(input_list)):
		for idx in range(len(input_list) - i - 1):
			if input_list[idx] > input_list[idx + 1]:
				input_list[idx], input_list[idx + 1] = input_list[idx + 1], input_list[idx]
	return input_list

print(bubble_sort(test_list))
