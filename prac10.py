# # program 1
# s2 = 'HelLo pYthOn'
# l=0
# u=0
# for i in s2:
#     if i.isupper():
#         u=u+1
#     elif i.islower():
#         l=l+1  
#     else:
#         l=l
#         u=u    
# print("No of upper case is",u)
# print("No of lower case is",l)

#Program 2

char = input("enter character that you have to find ")
para =("Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems.")
cnt = para.count(char)
print("Character "+char+" occured "+str(cnt)+" times in the given para")
