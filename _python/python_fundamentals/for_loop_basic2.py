#1
print("#### Biggie Size ####\n")
def biggie_size(input_list):
	for idx in range(len(input_list)):
		if input_list[idx] > -1:
			input_list[idx] = "big"
	return input_list
print(biggie_size([-1,3,5,-5]),"\n\n")


#2
print("#### Count Positives ####\n")
def count_positives(input_list):
	count = 0
	for idx in range(len(input_list)):
		if input_list[idx] > 0:
			count +=1
	input_list[len(input_list) - 1] = count
	return input_list

print(count_positives([-1,1,1,1]),"\n\n")

#3
print("#### sum total ####\n")
def sum_total(input_list):
	sum = 0
	for num in input_list:
		sum += num
	return sum

print(sum_total([1,2,3,4]),"\n\n")



#4
print("#### Average ####\n")
def average(input_list):
	sum = 0
	for value in  input_list:
		sum += value
	return sum/len(input_list)

print(average([1,2,3,4]),"\n\n")


#5
print("#### Length ####")
def length(input_list):
	length = 0
	for value in input_list:
		length += 1
	return length

print(length([37,2,1,-9]),"\n")
print(length([]),"\n\n")


#6
print("#### Minimum ####")
def minimum(list_input):
	if not list_input:
		return False

	min = list_input[0]
	for value in list_input:
		if min > value:
			min = value
	return min

print(minimum([37,2,1,-9]),"\n")
print(minimum([]),"\n\n")



#7
print("#### Maximum ####")
def maximum(input_list):
	if not input_list:
		return False

	max = input_list[0]
	for value in input_list:
		if max < value:
			max = value
	return max

print(maximum([37,2,1,-9]),"\n")
print(maximum([]),"\n\n")



#8
print("#### Ultimate Analysis ####")
def ultimate_analysis(list_input):
	if not list_input:
		return False

	analysis_results = dict(sumTotal = 0, average = 0
		,minimum = list_input[0], maximum = list_input[0], length = 0)
	for value in list_input:
		analysis_results["sumTotal"] += value
		analysis_results["length"] += 1
		if analysis_results["minimum"] > value:
			analysis_results["minimum"] = value
		if analysis_results["maximum"] < value:
			analysis_results["maximum"] = value

	analysis_results["average"] = analysis_results["sumTotal"]/analysis_results["length"]

	return analysis_results

print(ultimate_analysis([37,2,1,-9]))

#9
print("#### reverse list ####")
def reverse_list(input_list):
	if not input_list:
		return False

	for idx in range(int(len(input_list)/2)):
		temp = input_list[idx]
		input_list[idx] = input_list[len(input_list) - 1 - idx]
		input_list[len(input_list) - 1 - idx] = temp
	return input_list

print(reverse_list([37,2,1,-9]))
