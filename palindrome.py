 #Write a program to check whether the enetered string is palindrome or not.


str1 = input("Enter he string: ")
reverse_str = str1[-1::-1]

if str1 == reverse_str:
    print("The entered string is palindrome")
else:
    print("The entered string is not a palindrome")
