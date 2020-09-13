def sum(a,b):
    print (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def divide(a,b):
    return (a/b)
print("choose\n1:addition\n2:subtraction\n3:multiplication\n4:division")
choose=int(input('choose above number for required operation '))
input1=int(input('enter number 1  ='))
input2=int(input('enter number 2  ='))
if choose==1:
    (sum(input1,input2))
elif choose == 2:
    print(sub(input1, input2))
elif choose == 3:
    print(mul(input1, input2))
elif choose == 4:
    print(divide(input1, input2))
else:
    print('type valid numbers')