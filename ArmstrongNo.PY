u=int(input("Please enter any no"))
n=0
temp=u
while temp>0:
    digit=temp%10
    n+=digit**3
    temp=temp//10

if u==n:
    print("It is an armstrong no")
else:
    print("It is not an armstrong no")