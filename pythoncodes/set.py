# # a = {1,2,6,7,8}

# # print(a)

# # print(type(a))

# # s = {1,2,6,7,8,1}  #does'nt alow duplicate value

# # print(s)

# b = set([2,5,9,4,8])

# # print(b)

# c = set()

# # print(type(s))

# #it does'nt support indexing
# s = {1,2,3}
# s.add(3)

# # print(s)

# s.update([11,55,66])

# # print(s)

# s.update([5,6],[9,2])

# s.discard(55)

# # print(s)

# set  = {1,2,3,4,5}

# # set.pop()
# set.clear()
# # print(set)

# set1 = {1,2,3,4}
# set2 = {4,5,6,7}
# print( set1|set2)


# print(set1.union(set2))
# print(set1 & set2)

# print(set1.intersection(set2))

# print(set1-set2)

# print(set1.difference(set2))

# print(set1^set2)

# x= {"a","b","c","d"}
# y = {"c","d"}

# print(x.issubset(y))
# print(y.issubset(x))

# set3 = frozenset([1,2,3,4])
# set4 = frozenset([3,4,5,7])

# set1.add(5)

# print(set3)


name = ["anuj","luckay","niatin","prayag","archit"]
common = set(name[0])

for n in name[1:]:
    common &= set(n)


print(common)



