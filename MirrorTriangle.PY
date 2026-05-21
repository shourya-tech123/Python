u=int(input(("Enter the number of your choice :  ")))

for o in range(1, u+1):
    print("*" *o  + " "*( u - o)  +  " " + " " * (u - o) + "*" * o) 