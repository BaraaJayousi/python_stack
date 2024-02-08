test_list = [6,5,3,1,8,7,4,2]*800

def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        shift = 0
        for idx in range(i - 1, -1, -1):
            if(input_list[i - shift] < input_list[idx]):
                input_list[i -shift], input_list[idx] =  input_list[idx], input_list[i - shift]
                shift += 1
            else:
                break        
    return input_list

print(insertion_sort(test_list))

