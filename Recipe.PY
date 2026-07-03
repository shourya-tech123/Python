p =("Pasta Arrabiata", "Italian", 20, "Medium")
b =("Panner Biriyani", "Indian", 45, "Hard")


print("Recipe 1 : ", p)
print("Name of Recipe 1  : ", p[0])
print("Cuisine of Recipe 1  : ", p[1])
print(f"Prep time of Recipe 1  : {p[2]} minutes")
print("Difficulty level of Recipe 1  : ", p[-1])

print("\n")
print("*"*30)
print("\n")



all_tuples =(p,b)
print(f"First Recipe Name : {all_tuples[0][0]}")
print(f"Second Recipe Name : {all_tuples[1][0]}")
print(f"Second Recipe Prep time : {all_tuples[1][2]}")
print(f"Second Recipe Difficulty level : {all_tuples[1][3]}")

print("\n")
print("*"*30)
print("\n")

print("Ïterate/Loop through a tuple")
for detail in p:
    print("-", detail)

print("\n")
print("*"*30)
print("\n")

print("Enumerate through a turple")
for idx, detail in enumerate(b, start=1):
    print(f"{idx} : {detail}")

print("\n Tuple Unpacking ")
print("*"*30)
print("\n")

fruits =("apple", "banana", "kiwi", "orange", "guava")
f1,f2,f3,f4,f5 =fruits
print(f1)
print(f2)
print(f3)
print(f4)

x, *y =fruits
print(x)
print(y)

print(fruits.index("apple"))
print(fruits.count("apple"))

print("apple" in fruits)
print("apple" not in fruits)

t1 =(1,2,3)
t2 =("John", "David", "Mayank")

t3 =dict(zip(t1,t2))

print("\n")
print("*"*30)
print("\n")
for id, name in t3.items():
    print(f"{id} : {name}")

def process_report_card(subject, *marks):
    t=sum(marks)
    a =t/len(marks)

    if a >= 98:
        grade ="A"
    elif a >= 89:
        grade ="B"
    elif a >= 70:
        grade ="C"
    else:
        grade ="F"
    
    print(f"Report Card for: {subject}")
    print(f"Tuple recived: {marks}")
    print(f"Total marks: {t}")
    print(f"Average score: {a: .2f}")
    print(f"Final Grade: {grade}")

    process_report_card("Marks", 85, 90, 78, 82)








