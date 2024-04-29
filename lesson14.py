#lst = [4, 5, 2, 6, 8, 9, 7, 1, 3]
#
#
#length = len(lst) # buning bari divid conquer bolaklarga bolish
#for i in range(0, length):
#    for j in range(length - i - 1):
#        if lst[j] > lst[j + 1]:
#            lst[j], lst[j + 1] = lst[j + 1], lst[j]

#print(lst)
#
#
#lst = [1,2,2,3,4,4,5]
#lst1 = set(lst)
#lst2 = list(lst1)
#print(lst2)
#
#
#for x in lst:
#    if x not in lst1:
#        lst1.append(x)
#
#print(lst1)

def invert_list(lst):
    return [-x for x in lst]

lst = [1, 2, 3, 4, 5]
print(invert_list(lst))


tugma = input("yoz ;")
lst = ["red", "blue", "blue", "green"]

if tugma in lst:
    print(lst.index(tugma))


