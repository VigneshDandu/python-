'''for i in range(5):  # Outer loop
    for j in range(i):  # Inner loop dependent on outer loop
        print(f"Outer loop index: {i}, Inner loop index: {j}")'''

for i in range(1,10,5):
    for j in range(1,10):
      print (i,j)

for m in range(1,12):
    for n in range(1,m+1):
        print(  n ,end = " ")
    print()