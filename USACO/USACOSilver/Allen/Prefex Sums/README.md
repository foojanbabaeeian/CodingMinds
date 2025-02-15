Link to the actual docs:
https://docs.google.com/document/d/1CZrvm3pHn3qnnTBH37AooSbObvpeYzjIUgoAUy9vvDs/edit

# https://usaco.org/index.php?page=viewproblem2&cpid=57


'''
SAMPLE INPUT:
6 3
2
1
1
3
2
1
1 6
3 3
2 4
SAMPLE OUTPUT:
3 2 1
1 0 0
2 0 1
'''

https://usaco.org/index.php?page=viewproblem2&cpid=572
Breed Counting
1. Problem Recap:
You have a list of cows, each with a breed labeled as 1 (Holstein), 2 (Guernsey), or 3 (Jersey).
You need to answer several queries asking: "How many cows of each breed are there between two positions in the list?"
The goal is to answer these queries efficiently, even for large lists and many queries.
2. Why the Simple Approach is Too Slow:
A simple way to solve the problem is to count the number of 1's, 2's, and 3's for each query by scanning through the list between positions a and b for every query.
But if the list has up to 100,000 cows and we have 100,000 queries, this will take too long. Each query could take up to N steps, and for Q queries, that’s N * Q operations, which is too slow for large inputs.
3. Idea of Prefix Sums:
Instead of counting cows from scratch for each query, we can precompute how many cows of each breed appear from the start of the list up to any given point.
This way, when we get a query asking about cows between two positions, we can use these precomputed counts to answer the query in constant time (O(1)).
4. What is a Prefix Sum?:
A prefix sum tells you how many of something (in this case, cows of a certain breed) appear from the start of the list up to a specific position.
For example, if you want to know how many Holstein cows (breed 1) there are between positions 1 and b, the prefix sum tells you directly.
5. Precomputing the Prefix Sums:
We create three arrays: one for each breed (Holsteins, Guernseys, and Jerseys).
Each array tells us how many cows of that breed appear up to a certain position in the list.
For example, the value in the Holstein prefix array at position i tells us how many Holstein cows are there from the start to position i.
How do we build these arrays?:
We loop through the list of cows once, and for each cow, we add 1 to the correct breed's prefix sum.
By the end, we’ll have the total number of each breed up to every position in the list.
6. Using Prefix Sums to Answer Queries:
To find how many cows of each breed are between two positions a and b, we use the prefix sums:
To get the number of Holsteins in the range [a, b], subtract the prefix sum up to a-1 from the prefix sum up to b.
The same idea works for Guernseys and Jerseys.
Why does this work?:
The prefix sum up to b tells us the total number of cows of that breed from the start to position b.
The prefix sum up to a-1 tells us how many cows of that breed are before position a, so subtracting gives us the count from a to b.
7. Efficiency:
Building the prefix sum arrays takes O(N) time, since we only need to scan through the list once.
Once we have the prefix sums, each query can be answered in constant time (O(1)), because we’re just subtracting two numbers from the prefix arrays.
Overall, this approach is very efficient: it takes O(N) to set up the prefix sums, and O(1) to answer each of the Q queries, making the total time O(N + Q).
8. Example:
Suppose you have a list of cows: [2, 1, 1, 3, 2, 1] and a query asking for the count of cows between positions 2 and 4.
You would build the prefix sums for each breed:
Holstein prefix sum: [0, 0, 1, 2, 2, 2, 3]
Guernsey prefix sum: [0, 1, 1, 1, 1, 2, 2]
Jersey prefix sum: [0, 0, 0, 0, 1, 1, 1]
For the query (2, 4), you would:
Get Holsteins in [2, 4]: Holsteins[4] - Holsteins[1] = 2 - 0 = 2
Get Guernseys in [2, 4]: Guernseys[4] - Guernseys[1] = 1 - 1 = 0
Get Jerseys in [2, 4]: Jerseys[4] - Jerseys[1] = 1 - 0 = 1
The result is 2 0 1.


https://usaco.org/index.php?page=viewproblem2&cpid=595

Homework:

Problems to work on for next week:
USACO 2016 January Contest, Silver
Problem 2. Subsequences Summing to Sevens
https://usaco.org/index.php?page=viewproblem2&cpid=595


USACO 2017 February Contest, Silver
Problem 3. Why Did the Cow Cross the Road III
https://usaco.org/index.php?page=viewproblem2&cpid=716

