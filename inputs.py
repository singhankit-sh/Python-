#inputs in python 
name = input(" Enter your age: ")
print("you entered", name)

# input() result is always str
val = input(" enter some value: ")
print(type(val), val) # str 

#for appropriate use type casting
int("20")
val = int(input(" enter some value: "))
print(type(val), val)

# float
int("20")
val = float(input(" enter some value: "))
print(type(val), val)

#print age marks and name 
name = input("enter name: ")
age = input("enter age: ")
marks = input("enter marks: ")

print("welcome", name)
print("i entered", age)
print("I got", marks)


