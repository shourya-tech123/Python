o =int(input("Please enter no of rows: "))

for i in range(1, o+1):
    print(" "*(o-i)+"* "*i)
for j in range(o-1,0,-1):
    print(" "*(o-j)+"* "*j)