def sidneySort(booHoo):
    # take the thing and check if the next is smaller or bigger
        # if smaller swap  

    for i in range(len(booHoo)):
        for j in range(len(booHoo)-1):
            if booHoo[j+1] < booHoo[j]:
                booHoo[j], booHoo[j+1] = booHoo[j+1], booHoo[j]
    return booHoo 
print(sidneySort([21,-23,2,1]))