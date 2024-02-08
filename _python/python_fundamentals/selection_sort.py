test_list = [3,1,0,4,2,5,6,7,8]*80
def selection_sort(input_list):
    for i in range (len(input_list)):
        min_idx = i
        for idx in range(i,len(input_list)):
            if input_list[min_idx] > input_list[idx]:
                min_idx = idx
        input_list[i], input_list[min_idx] = input_list[min_idx], input_list[i]
    return input_list

print(selection_sort(test_list))