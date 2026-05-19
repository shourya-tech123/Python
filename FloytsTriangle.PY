u =int(input("Please enter the no of rows: "))
n=1
for i in range(u):
    for j in range(i+1):
        print(n, end=" ") 
        n=n+1
    print()
