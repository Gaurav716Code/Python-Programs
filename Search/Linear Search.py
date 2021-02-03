def linearsearch(data, x):
    for i in range(len(data)):
        if data [i] == x:
            return True
        return False


LT = [20,41,8,45,10,63,98]
x = 10

print("element found : " + str(linearsearch(LT,x)))


#print("element found at index " + str(linearsearch(LT,x)))
