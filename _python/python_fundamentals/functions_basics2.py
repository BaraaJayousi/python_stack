#1
print("#### Start Countdown Function ####\n")
def countdown(input):
	list_output = []
	for num in range(input, -1, -1):
		list_output.append(num)
	return list_output

print(countdown(10),"\n\n")

#2
print("#### Start Print and  Return ####\n")
def print_return(list_of_two_nums):
	if(len(list_of_two_nums) == 2):
		print(list_of_two_nums[0])
		return list_of_two_nums[1]
	else:
		print("Please input a list of two entries")
		return None

print(print_return([1,3]),"\n\n")

#3
print("#### Start First Plus Length ####\n")
def first_plus_length(list_input):
	return list_input[0] + len(list_input)
print(first_plus_length([1,2,3,4,5]),"\n\n")


#4
print("#### Start Values greater than second ####\n")
def values_greater_than_second(list_input):
	list_output = []
	count = 0
	for input in list_input:
		if input > list_input[1]:
			count+=1
			list_output.append(input)
	print(count)
	return list_output


print(values_greater_than_second([5,2,3,2,1,4]),"\n")


#5
print("#### Start This Length, That Value ####\n")
def this_length_this_value(size, value):
	list_output = []
	for i in  range(size):
		list_output.append(value)
	return list_output

print(this_length_this_value(4,7))
print(this_length_this_value(6,2))

