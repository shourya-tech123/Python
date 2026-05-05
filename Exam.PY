h =input("Please enter yes for medical cause and no for healthy")
if h=="Yes":
    print("You can attend the exam")
else:
    a = int(input("Please enter your attendence"))
    if a>=75:
        print("You can write the exam")
    else:
        print("You are not eligible to write the exam")



