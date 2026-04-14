print("Please enter your marks in 4 Subjects")
maths=int(input("Enter Maths marks"))
english=int(input("Enter english marks"))
science=int(input("Enter science marks"))
sst=int(input("Enter sst marks"))

sum=maths+english+science+sst
print("sum of the subjects", sum)

perc=(sum/400)*100
print("perc of the subjects", perc,"%")