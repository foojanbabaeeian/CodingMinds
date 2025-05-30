# ant problem 

# On a stcik of ants, each ant has a position and a direction (left or right).
# When two ants collide, they simply reverse direction.
# variables for ant 
ants = {20:"r", 30:"r", 50:"r", 60:"l", 80:"r"}  # positions of the ants

# -------------------------------------------------
#     jack    bella lily liliana     josh

# every second is the iteration of the loop 
# while len(ants) > 1:  # while there are more than one ant
#     for key in list(ants.keys()):
#         key +=1 if ants[key] == "r" else -1
#         for thiskey in list(ants.keys()):
#             for otherkey in list(ants.keys()):
#                 if thiskey + 1 == otherkey or thiskey - 1 == otherkey:
                    