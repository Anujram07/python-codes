list0 = [4,5,0,0,7,8,0,5,0,4,0]
arr = []

for i in list0:
    if(i == 0):
        list0.remove(i)
        arr.append(i)
    
list0.extend(arr)
# print(list0)



name = ["anuj","lucky","nitin","prayag","deepak"]
char = input("Enter a alphabet:-")
names = []
count = 0

for x in name:
    if char in  x:
        names.append(x)
        count = count + x.count(char)
        

if count > 0:
    print(char , " -> " , count , "in ", names )
else:
    print("Alphabet not found")

