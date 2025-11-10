list0 = [4,5,0,0,7,8,0,5,0,4,0]
arr = []

for i in list0:
    if(i == 0):
        list0.remove(i)
        arr.append(i)
    
list0.extend(arr)
print(list0)