# # l1=[0,1,2,3,4,5,6]
# # print(l1)
# # del(l1[3])
# # print(l1)
# # l1.remove(6)
# # print(l1)
# # e=l1.pop(4)
# # print(e)
# # l1.clear()
# # print(l1)



# d1={1:'A',2:'B',3:"C",4:'D',5:'E'}

# d2=d1.copy()
# print(d2)

# print(d1.get(3))

# print(d1.items())

# print(d1.keys())

# print(d1.values())

# d3=d1.popitem()
# print(d3)
# print(d1)

# d4=dict.fromkeys(['a','b','c'],1)
# print(d4)

# d5=d1.pop(4)
# print(d5)
# print(d1)

# d1.update({6:'f',7:'g'})
# print(d1)

# d6=d1.clear()
# print(d1)

# l1=['1','2','3','4','5']
# print(l1)

# a=[1,2,3,4,5]
# b=['a','d','c']
# a.extend(b)
# print(a)

t1=(1,2,3,4,5,6,5,5,5,5,5)
print(t1[-1])
print(t1[2:4])
print(t1[:])
print(t1[2:])
print(t1[:-2])
x=t1.index(5) #returns the index of the specified input
x=t1.count(5) #count the number of times the char has repeated
print(x)