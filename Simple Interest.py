def calSI():
    # input principal amount as P
    P = float(input("Enter Your Principal Amount : Rs."))
    # input rate of interest per month as R
    R = float(input("Enter Your Rate of Interest Per Month :"))
    #input number of months as N
    N = int(input("Enter Loan Months :"))

    #Calculate Simple Interest as SI =(P * N * R)/100
    SI = (P * N * R)/100

    #Calculate Total Amount as Amt = P + SI
    Amt = P + SI

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #print principal amount
    print("Principal Amount Rs.",P)
    #print rate of interest
    print("Rate of Interest : ",R)
    #print number of months
    print("Number of Months : ",N)
    #print Simple interest
    print("Simple Interest : Rs.",SI)
    #print Amount
    print("Amount : Rs.",Amt)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

calSI()
