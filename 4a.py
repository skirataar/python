def insertion_sort(arr,n):
   for i in range(1,n):
       key = arr[i]
       j = i-1
       while j>=0 and key < arr[j]:
           arr[j+1] = arr[j]
           j -=1
       arr[j+1] = key
   return arr
 
def merge_sort(arr):
   n = len(arr)
   if(n>1):
       mid = n//2
       L = arr[:mid]
       R = arr[mid:]
       merge_sort(L)
       merge_sort(R)
       
       i = j = k = 0
       while i<len(L) and j<len(R):
           if L[i]<=R[j]:
               arr[k] = L[i]
               i+=1
           else:
               arr[k] = R[j]
               j+=1
           k+=1
       while(i<len(L)):
           arr[k] = L[i]
           k+=1
           i+=1
       while(j<len(R)):
           arr[k] = R[j]
           k+=1
           j+=1
 
n = int(input("Enter the size of array"))
arr = [None]*n
print("Enter the elements")
for i in range(n):
   arr[i] = int(input())
print("Before Sorting : ",arr)
merge_sort(arr)
print("After Merge Sort : ",arr)
insertion_sort(arr,n)
print("After Insertion sort : ",arr)