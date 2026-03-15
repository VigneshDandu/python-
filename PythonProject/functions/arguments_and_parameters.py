
def maths(a: int,b:int) -> int:
    c = a + b
    print(c)
    return c

maths(10,29)

print(f"the sum of two numbers is {maths(10,46)}")

def prime(n):
    for i in range(2,n):
        if n%i ==0:
            print('not prime')
            break
        else:
            print('prime')
            break
    return print
prime(10)