for i in range(1,6):
    for j in range(5,i,-1):
        print(" ", end = " ")
    for k in range(i):
        print("*" , end = " ")
    print()


for i in range(1, 6):
    print("  " * (5 - i) + "* " * i)