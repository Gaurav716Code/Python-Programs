# Selection Sort Descending
def selectionSort( data ):
    n = len( data )
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if data[j] > data[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = data[i]
            data[i] = data[minValueIndex]
            data[minValueIndex] = temp

    return data


data = [13, 10, 4, 65, 29, 73, 57]
print("Unsorted list: ", (data))
selectionSort(data)
print("Selection sorted list in descending: ", (data))
