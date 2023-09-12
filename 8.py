class A:
    def Pal(self, val:str):
        if(val!=val[::-1]):
            print("Not palindrome")
        else:
            print("Is Palindrome")
        
class B(A):
    def Pal(self, val:int):
        super().Pal(str(val))
    
A().Pal(input("enter  String"))
B().Pal(int(input("enter  Number")))
