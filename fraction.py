
# generates all rearrangements of list

def rearrangements(elements):
    if len(elements) <= 1:
        yield elements
        return
    for i in range(len(elements)):
        temp = elements.copy()
        temp.pop(i)
        for j in rearrangements(temp):
            yield elements[i:i+1] + j


a = rearrangements([i for i in range(1,10)]) # iterable of all rearrangements of integers 1 \leq x \leq 10

epsilon = 10**(-8) # margin of error (eliminates floating pt errors like 0.9999999 \neq 1)

# checks each rearrangement
# prints out list of numbers such that a / bc + ... = 1
# it returns all results that meet this criteria but they are all identical (just different ordering)
for i in a:
    val = (i[0] / (i[1] * i[2])) + (i[3] / (i[4] * i[5])) + (i[6] / (i[7] * i[8]))
    if abs(1 - val) < epsilon:
        print([j for j in i])






# random algorithm

# import random

# lst = [1,2,3,4,5,6,7,8,9]
# epsilon = 10**(-8)

# while True:
#     random.shuffle(lst)
#     val = (lst[0] / (lst[1] * lst[2])) + (lst[3] / (lst[4] * lst[5])) + (lst[6] / (lst[7] * lst[8]))
#     if abs(1 - val) < epsilon:
#         print([j for j in lst])





