import numpy
x=input('Enter the matrix')
x=list(x.split(' '))
x=list(map(int,x))
while True:
    temp=int(input('Enter the index'))
    for i in range(len(x)):
        if i==temp:
            if x[i]==0:
                x[i]=1
            elif x[i]==1:
                x[i]=0
    print(x)
    if all([j for j in x if j==0]):
        break
print(x)