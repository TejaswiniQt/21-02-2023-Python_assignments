#Write a Python program to determine whether a number is binary.



num = int(input("Enter the number: "))
while(num>0):
    res = 0
    digit = num % 10
    if digit != 0 and digit != 1:
        res = 1
        break
    num = num // 10

if res == 1:
    print("The enetered number is not a binary number")
else:
    print("The entered number is binary number")
