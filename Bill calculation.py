def bill():
    #Input product name as product
    product = str(input("Enter product name :"))
    #input quantity as quantity
    quantity = int(input("Base Quantity :"))
    #input base price / price per unit as ppu
    ppu = float(input("Price per unit :"))
    cb = (quantity*ppu)
    print("Basic Bill :", cb)
    print("GST : 18%")
    print("Price Including GST :", cb + cb*0.18)

bill()
    
