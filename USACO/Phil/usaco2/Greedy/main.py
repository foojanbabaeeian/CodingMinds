'''
There are n houses for sale, with the price of each houses stored in a list price. You have a budget of budget dollars to spend.

Return the maximum number of houses you can buy.

Example 1:


budget = 100
prices = [20, 90, 40, 90]

# output: 2
# With budget of 100 we can buy the $20 and $40 houses
print(allocation(prices, budget))
Example 2:


budget = 50
prices = [30, 10, 10, 30]

# output: 3
# With budget of 50 we can buy two $10 and one $30 houses
print(allocation(prices, budget))
'''
budget = 50
prices = [30, 10, 10, 30]
prices.sort()
x=0
y=0
for i in prices:
    if x> budget:
        break
    x+=i
    y+=1
    budget-=i
    
print(y)
