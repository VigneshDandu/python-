# #ask user for temperature in Celsius and convert to Fahrenheit: F = (C × 9/5) + 32
# temp = float(input("Enter temperature in Celsius: "))

# F = (temp* (9/5))+32
# print("the farhenheit for celcius input is" ,F)

# #Take two numbers as input and print their sum, difference, product, and division

# a = float(input("num1 :"))
# b = float(input("num2 :"))

# print("sum:",a+b)
# print("difference :",a-b)
# print("product :",a*b)
# print("div :",a/b)0


# #Ask for hours worked and hourly rate, calculate total pay.

# hour = float(input("enter hour: "))
# rate = float(input("hourly rate : "))


# print("total pay according to the worked hours and hourly rate is: ",hour*rate)

#Calculate how many hours and minutes are in 250 minutes total

t = 250.0
hm =t/60
fhm=t//60
m = (hm -fhm)*60

print("minutes: ",m)
print("hours: ",fhm)

#Check if a number is divisible by both 3 and 5.

num = int(input("to check if number is divisible by 3 and 5 :"))
if num%3==0 and num%5==0 :
    print("divisible by 3 and 5",num)
else:
    print("not divisible by 3 and 5")
