s=input("Please enter any word: ")
char=input("Please enter any character: ")
c=0
i=0
while(i<len(s)):
    if s[i]==char:
        c=c+1
    i=i+1
print("Your character", char,"Has occured", c)