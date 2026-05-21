n=float(input(("Enter the any decimal number:  ")))

b=""
for i in range(10):
    if n > 0:
     b = str(n % 2)+b
     n = n//2
print("The Binary Number is", b)

