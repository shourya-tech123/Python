u =int(input("Please enter units used"))
if u<50:
    print("you must pay",u*3,"rupees")
elif u>=50 and u<=100:
    print("You must pay", u*6,"rupees")
elif u>100 and u<=200:
    print("You must pay", u*19,"rupees")
else:
    print("You must pay", u*30,"rupees")