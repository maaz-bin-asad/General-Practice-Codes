x=input('Enter the array')
x=list(x.split(' '))
x=list(map(int,x))
y=int(input('Enter the number'))
temp=0
temp3=0
i=0
if y in x:
    print(y)
else:
    while True:
        incremented=y+i      #Check all nearest values
        decremented=y-i
        if incremented in x:
            temp=1  #Acting as a flag
            break
        if decremented in x:
            temp3=2  # Acting as a flag
            break
        i=i+1
if temp==1:
    print(incremented)
if temp3==2:
    print(decremented)
