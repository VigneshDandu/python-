for i in range(1,6):
    for j in range (1,6):
        if j<=i:
            print( j,end =" ")
    print()
"""
1
12
123
1234
12345"""

for m in range(1,6):
    for n in range(1,6):
        if n<=m:
            print(m,end =" ")
    print()
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 '''

for x in range(1,6):
    for y in range(1,6):
        if x<=y:
            print(x,end =" ")
    print()
"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
"""
for f in range(1,5):
    for g in range(5,f,-1):
        print(f,end = " ")
    print()