# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name11 = name1.lower()
name21 = name2.lower()
# print(name11)
# print(name21)

t = name11.count("t") + name21.count("t")
r = name11.count("r") + name21.count("r")
u = name11.count("u") + name21.count("u")
e = name11.count("e") + name21.count("e")

l = name11.count("l") + name21.count("l")
o = name11.count("o") + name21.count("o")
v = name11.count("v") + name21.count("v")
e = name11.count("e") + name21.count("e")

firstColumn = t+r+u+e
secondColumn = l+o+v+e
# print(firstColumn)
# print(secondColumn)
numberInt = str(firstColumn) + str(secondColumn)
# print(numberInt)
number = int(numberInt)
# print(number)
# print(type(number))
if number < 10 or number > 90:
    print(f"Your score is {number}, you go together like coke and mentos.")
elif number >= 40 and number <= 50:
    print(f"Your score is {number}, you are alright together.")
else:
    print(f"Your score is {number}.")
