#Bubble Sort Descending
def bubble_sort(data):
   
    for i in range(len(data)):
        
        for j in range(len(data) - 1):
            if data[j] < data[j+1]:
            
                data[j], data[j+1] = data[j+1], data[j]


data = [13, 10, 4, 65, 29, 73, 57]
print("Unsorted list: ", (data))
bubble_sort(data)
print("Bubble sorted list in descending: ", (data)) 
