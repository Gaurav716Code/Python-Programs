def looprangeno():
    start = int(input("Enter Starting Number :"))
    stop = int(input("Enter Stoping Number :"))
    condition = int(input("Enter Condition Number for Sequence :"))
    for var in range(start,stop,condition):
        print(var,end=',')
    


looprangeno()
