l1 = [1,2,3]
l2 = [4,5,6]
l3 = []
l1.extend(l2) #extend no lugar de append para apenas extender não enfiar uma lista na outra 
l3 += l1
print(l1)
