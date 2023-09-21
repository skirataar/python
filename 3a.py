sentence = input("Enter a sentence : ")
digCnt = upCnt = loCnt =wordcnt=0
wordcont=sentence.split()
for ch in sentence:
   if ch>='0' and ch<='9':
      digCnt += 1
   if ch>='A'and ch<='Z':
      upCnt += 1
   if ch>='a' and ch<='z':
      loCnt += 1
 
print("This sentence has\n")
print("words: ", len(wordcont),"\n" "digits",digCnt, )
print("upper case letters",upCnt, "\n" "lower case letters ",loCnt)