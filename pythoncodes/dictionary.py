my_dict ={}

my_dict ={1:"abc",2:"def",3:"xyz"}

# print(my_dict)

my_dict2 = {'name':'satish',1:['abc','xyz']}
# print(my_dict2)

# dict3 = dict()

# print(my_dict2.get('name'))
# print(my_dict2.get('avg'))

d1 = {'name':'satish','age':25}

d1['degree'] = 'mtech'

# print(d1)

d1.popitem()
# print(d1)

squares = {2:4,3:9,4:10,5:25}

# del squares[2]

# print(squares)

# squares.clear()

# print(squares)

# del squares

# print(squares)


# subjects = {}.fromkeys(['Math','physics','science'],0)
# print(subjects)

d = {1:5,2:10,3:15,4:20,5:25}

# print(subjects.items())
# print(subjects.keys())
# print(subjects.values())

# for pair in d1  .items():
#     print(pair)

d4 ={k:v for k,v in d.items() if v > 2}
print(d4)