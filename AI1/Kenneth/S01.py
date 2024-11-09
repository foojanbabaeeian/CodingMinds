# Python review
# data types:
    # Booleans -> True and False 
    # Strings ->  Anything in "" , '', -> Quotations 
    # Numbers ->   
        # float -> 3.14159265
        # integers -> 3, -5, 7

# Logical Operator 
# AND 
# T T -> T
# T F -> F
# F F -> F

# OR
# T T -> T
# T F -> T
# F F -> F

# NOT
# T -> F
# F -> T


# Relational Operators
# Less Than or Equal To (<=)
# Less Than (<)
# Equal To (==) - not to be confused with =, which is the assignment operator.
# Not Equal To (!=)
# Greater Than (>)
# Greater Than or Equal To (>=)

# if statements 
Kenneth = "Happy"
if Kenneth == "Happy":
    print("Clap your hands")

grade = 45

if grade <= 100 and grade >= 90:
    print("A")
elif grade < 90 and grade >= 80:
    print("B")
elif grade < 80 and grade >= 70:
    print("C")
elif grade < 70 and grade >= 60:
    print("D")
else:
    print("F")

# loops 
    # while loop
count = 0
while count <6:
    print(count)
    count += 1

    # for loops 
for i in range(6):
    print(i)

# Lists 
user_list = ["Adam", "Brianna", "Cole"]
# adding 
user_list.append("Kody")
# remove
user_list.remove("Adam")

user_list.pop(4)
for i in user_list:
    print(i)