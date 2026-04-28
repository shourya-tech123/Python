print("Please enter the marks in 5 subjects")

m1= int(input("Enter English Marks"))
m2= int(input("Enter Hindi Marks"))
m3= int(input("Enter Maths Marks"))
m4= int(input("Enter Science Marks"))
m5= int(input("Enter Social Studies Marks"))

t = m1+m2+m3+m4+m5
avg = t/5

if avg >=91 and avg <=100:
    print("Your grade is A1")
elif avg >=81 and avg <=90:
    print("Your grade is A2")

elif avg >=71 and avg <=80:
    print("Your grade is B1")

elif avg >=61 and avg <=70:
    print("Your grade is B2")

elif avg >=51 and avg <=60:
    print("Your grade is C1")

elif avg >=41 and avg <=50:
    print("Your grade is C2")

elif avg >=31 and avg <=40:
    print("Your grade is D1")

elif avg >=21 and avg <=30:
    print("Your grade is D2")

elif avg >=11 and avg <=20:
    print("Your grade is E1")

elif avg >=1 and avg <=10:
    print("Your grade is E2")

else:
    print("Invaild Input")


 