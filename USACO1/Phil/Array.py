'''
What are the indices of the elements "Apple", "Bread", and "Milk"?

python
food = ["Apple", "Shrimp", "Pineapple", "Bread", "Eggs", "Milk"]
'''
food = ["Apple", "Shrimp", "Pineapple", "Bread", "Eggs", "Milk"]

lookfor= ["Apple", "Bread", "Milk"]
indix = []
for i in range(len(food)):
    if food[i] in lookfor:
        indix.append(i)
'''
Problem 5
What is the problem with the following code?

python
names = ["Kevin", "Chris", "Mayami"]
print(names[10])
'''
names = ["Kevin", "Chris", "Mayami"]
print(names[10])