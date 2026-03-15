#iteration using for loop
b = ["ram","laxman","parab","suvitra","jash"]
for i in b:
    print(i)
print(len(b))
#iteration using for loop with range and length function

for i in range(len(b)):
    print(b[i])

print("")

#iteration using while loop
i=0
temp = len(b)-1
while i <= temp:
    print(b[(i)])
    i+=1