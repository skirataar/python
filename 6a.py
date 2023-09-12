fname = input("Enter the filename : ")      
infile = open(fname, "r")
line= int(input("Enter the first N line "))
for x in range(line):
    a = infile.readline()
    print(x+1,":",a)
infile.seek(0)
word = input("Enter a word : ")
cnt = 0
for line in infile:
    r=line.split()
    cnt += r.count(word)
print("The word", word, "appears", cnt, "times in the file")
