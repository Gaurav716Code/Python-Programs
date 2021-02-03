def binary_search(data_list,item):
    first = 0
    last = len(data_list)-1
    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        if data_list[mid] == item :
            found = True

        else:
            if item < data_list[mid]:
                last = mid -1
            else:
                first = mid +1
    return found

print(binary_search([10,67,92,105,128], 128))
