l=[]
for i in range(3):
    l.append(int(input(f"Enter marks {i+1}: ")))

l.sort()

avg = (l[1]+l[2])/2
print(avg)