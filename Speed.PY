x =int(input("Please enter speed of x"))
y =int(input("Please enter speed of y"))
z =int(input("Please enter speed of z"))

t = x+y+z
avg=t/3

print(avg)

if avg>x and avg> y and avg> z:
    print("Avg is greater than x,y and z ")
elif avg>x and avg>y:
    print("Avg is greater than x and y")
elif avg>x and avg>z:
    print("Avg is greater than x and z")
elif avg>y and avg>z:
    print("Avg is greater than y and z")
elif avg>x:
    print("Avg is greater than x")
elif avg>y:
    print("Avg is greater than y")
elif avg>z:
    print("Avg is greater than z")
else:
    print("Invaild Speed")