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
# budget = 50
# prices = [30, 10, 10, 30]
# prices.sort()
# x=0
# y=0
# for i in prices:
#     if x> budget:
#         break
#     x+=i
#     y+=1
#     budget-=i
    
# print(y)


'''
Problem Statement
Given n activities with their start and finish times, what the the maximum number of activities that can be performed, assuming the activities have to be performed one at a time?

Return the maximum number of activities that can be completed.
z
Example 1:

Activities	a	b	c	d	e	f	g	h	i	j	k
Start Time	1	3	0	5	3	5	6	8	8	2	12
Finish Time	4	5	6	7	8	9	10	11	12	13	14
What is the maximum number of activities that can be completed?

Activities {c, i, k} can be completed
Activities {a, d, h, k} can also be completed, and larger than the previous solution.
It is also not unique, consider activities {b, d, i, k}.
How would you approach this problem? Does any of the following greedy strategies work?

Choose the longest activity first
Choose the shortest activity first
Choose the activity that start the earliest first
Choose the activity that finish the earliest first
Solution
Early Finish Greedy Strategy:

Sort the activities by finish time
Schedule the first activity
Schedule the next activity (in the sorted list) which starts after the previous activity finishes (first non-conflicting task)
Repeat until there are no more activities.
'''

# start_time = {1:4 , 3:5 , 0:6 , 5:7 , 3:8 , 5:9 , 6:10 , 8:11 , 8:12 , 2:13 , 12:14}
# starttime=0
# ans=0
# print(start_time)
# for start, end in start_time.items():
#     if start >= starttime:
#         ans+=1
#         starttime=end
#         print(start, end, starttime)
# print(ans)

def activity_selection(start, finish):
    # Pair each activity with its start and finish times
    activities = sorted(zip(start, finish), key=lambda x: x[1])  # sort by finish time

    count = 1  # always select the first activity
    last_end_time = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            count += 1
            last_end_time = activities[i][1]

    return count

start =  [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
finish = [4, 5, 6, 7, 8, 9,10,11,12,13,14]

print(activity_selection(start, finish))  # Output: 4
