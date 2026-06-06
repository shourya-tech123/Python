def printfullname(First_name ,Last_Name ,Greet="Hi"):
    return f"{Greet} {First_name} {Last_Name}"
fname=input("Enter your First Name :")
lname=input("Enter your Last Name :")
greeting=input("Enter Greeting :")

fullname=printfullname(fname,lname,greeting)
print(f"Your fullname is {fullname}" )