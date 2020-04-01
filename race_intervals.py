def calc():
    param=input('Enter parameters')
    param=list(map(int,list(param.split(' '))))
    intervel=input('Enter intervels')
    intervel=list(map(int,list(intervel.split(' '))))
    temp=list()
    for first in range(0,len(intervel),1):
        for second in range(i,len(intervel),1):
            for third in range(first,second+1,1):
            	intervel[third]=list(intervel[third])
    	        for sum in intervel:
    	        	if sum in intervel[third]:
    	        		continue:
    	        	else:
    	        		summ=summ+sum
    	        temp.append(summ)
test_cases=int(input('Enter test cases'))
for tests in range(0,test_cases):
	calc()
	
	