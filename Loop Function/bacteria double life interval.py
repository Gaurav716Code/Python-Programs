def bacteriaDoubleLife():
    time = 0
    pop = int(input("Enter population of bacteria : "))
    rate = float(input("Enter growth rate : "))
    dubPop = pop*2
    while pop <= dubPop :
        pop = pop + (pop*rate)
        time = time+1
        
    print("Bacteria Population : ",round(pop))
    print("Bacteria doubling time : ",time," min.")

bacteriaDoubleLife()
