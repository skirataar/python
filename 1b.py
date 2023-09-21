num=input("Enter the Number")

if (num==num[::-1]):
   print("The Number is Palindrome", num)
else:
   print("The Number  is not Palindrome")
for i in set(num):
     print(i, "appears", num.count(str(i)),"times")