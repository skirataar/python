def Bin2dec(bin):
   l=len(bin)
   dec=0
   for i in range(l):
       dec+=int(bin[i])*(2**(l-i-1))
   return dec
 
 
def oct2hex(oct):
   l=len(oct)
   dec=0
   for i in range(l):
       dec+=int(oct[i])*(8**(l-i-1))
   hexa=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
   octhex=' '
   while dec>0:
       rem=dec%16
       octhex=hexa[rem]+octhex
       dec=dec//16
   return octhex
       
bin=input("Enter the Binary Number")
print("Binary to Decimal is ",Bin2dec(bin))
oct=input("Enter the octal Number")
print("Octal to Decimal is ",oct2hex(oct))