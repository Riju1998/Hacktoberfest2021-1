print("Find the g.c.d and l.c.m of two numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    temp = a
    a = b
    b = temp
# print("a","=",a,"& b","=",b)
i = a
while i >= 0:
    if b % i == 0 and a % i == 0:
        break
    i -= 1
print("The required g.c.d is: ", i)
i = 1
while i <= a:
    l = a * i
    if l % b == 0:
        break
    i += 1
    print("The required l.c.m is: ", l)
