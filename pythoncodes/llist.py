lst1 = ["mango","papaya","apple","banana","litchi"]

lst2 = [1,8,7,2,9]

# print(lst1[0])
# print(lst2[0])
# print(lst1[-1])
# print(lst2[-1])


# print(lst1)

# for i in lst1:
    # print(i)

lst1.append("amrood")
# print(lst1)


# for i in lst1:
#     print("I Like ", i)


lst1.insert(2,"Grapes")
# print(lst1)

lst1.remove("mango")
# print(lst1)

lst1.pop()
# print(lst1)

# A = [1,2]
# B = [3,4]

# print(A+B)
# if "mango" in lst1:
#     print("yes")
# else:
#     print("no")
sum = 0
avg = 0
for i in lst2:
    sum = sum +i



avg = sum / len(lst2)
# print(sum)
# print(avg)
# print(min(lst2))
# print(max(lst2))

lst2.append(1)
lst2.append(8)
lst2.append(9)
lst2.append(9)
lst2.append(9)
lst2.append(2)

# print(lst2)

# print(lst2.count(9))


char = ['A','B','C','B','A']
# print(char.index('C'))


lst1.reverse()
# print(lst1)

# for fruit in lst1:
    # print(fruit.upper())

lst4 = [10,20,30,40,50,60,70,80]
# print(lst4[:])
# print(lst4[0::2])

num = [2,5,9,2,4,4,2]
num2 = []

# for i in num:
#     val = i
#     if val in range(1+1,len(num)):
#         if val not in num2:
#             num2.append(val)
#         num.remove(i)



# print(num)
# print(num2)


# Two Sum problem
numList = [4,9,2,4,5,7,2,1]
# target = int(input("Enter a target:-"))

# for i in numList:
#     remain = target-i
#     if remain in range(i+1,len(numList)):
#         a = i
#         b= remain
#         break

# print(a , " " , b)



# runnung sum problem 
run = [1,2,3,4,5]
sum = 0
run2 = []
for i in run:
     sum = sum + i
     run2.append(sum)
# print(run2)



list0 = [4,5,0,0,7,8,0,5,0,4,0]
arr = []

for i in list0:
    if(i == 0):
        list0.remove(i)
        arr.append(i)
    list0.extend(arr)

print(list0)