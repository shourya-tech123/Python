L =[4,5,1,2,9,7,10,8]
print("Original List: ", L)

total=0

for i in L:
    total+=1

avg= total/len(L)

print("sum = ", total)
print("average = ", avg)

L.sort()

print("Smallest element is:", L[0])
print("Smallest element is:", min(L))

print("Largest element is:", L[-1])
print("Largest element is:", max(L))

