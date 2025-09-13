'''P11-6 Exercise: Merge Two Sorted Linked Lists
Problem Statement
Leetcode Merge Two Sorted Lists

Given the heads of two sorted linked lists, list1 and list2.

Merge the two linked lists together into one sorted linked list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

The definition of the linked list is the following:


class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next
Example 1:


# The arrows represent the pointers of the nodes.
list1 = [1 -> 2 -> 6]
list2 = [1 -> 3 -> 10]

# output: [1 -> 1 -> 2 -> 3 -> 6 -> 10]
print(mergeLinkedLists(list1, list2))
Example 2:


list1 = []
list2 = [4 -> 9 -> 10]

# output: [4 -> 9 -> 10]
print(mergeLinkedLists(list1, list2))

'''

# list1 = [1 -> 2 -> 6]
# list2 = [1 -> 3 -> 10]

# output: [1 -> 1 -> 2 -> 3 -> 6 -> 10]
print(ml(list1, list2))

class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next
def ml(list1,list2):
    temp = list1.head
    tempa = list2.head
    tempswap = list2.head
    while temp!=None and tempa!= None:
        if temp <= tempa:
            temp.next
        elif temp == tempa:
            tempa.next = temp.next
            temp.next=tempa
            
        


