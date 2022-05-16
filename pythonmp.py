


def add(a,b):
    result=a+b
    print(result)

def substract(a,b):
    result=a-b
    print(result)    

def multiply(a,b):
    result=a*b
    print(result)

def divide(a,b):
    result=a/b
    print(result)    

a=int(input("enter value"))
op=input("enter operator")
if op == '+' or op == '-' or op == '*' or op == '/':
    b=int(input("enter value"))

    if op == '+':
       add(a,b)
    elif op == '-':
       substract(a,b)
    elif op == '*':
       multiply(a,b)
    elif op == '/':
       divide(a,b)
    else:
        print("null")   
else:
    print("invalid operator")                