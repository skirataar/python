def Fibonacci(n):
   if n==1:
       return 0
   elif n==2:
       return 1
   else:
       return (Fibonacci(n-1)+Fibonacci(n-2))
   
 
num=int(input("Enter the number\n"))
if num>0:
   res=Fibonacci(num)
   print("Fibonacci of ", num ,"is",res)
else:
   print("Error in the input")