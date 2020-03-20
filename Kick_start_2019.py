def count(args,n):
    args.remove((n))   #remove maximum from list
    hours=list()
    for i in args:
        count=0
        while i!=n:
            i=i+1
            count=count+1   #count the hours
        hours.append(count)
        count=0
    return sum(hours)
test_cases = int(input())
final=list()
for i in range(test_cases):
    team = input()
    team = list(team.split(' '))
    team = list(map(int, team))
    skill = input()
    skill = list(skill.split(' '))
    temp=int(skill[1])
    skill = ('').join(skill[:temp])
    skill = list(skill)
    skill=list(map(int,skill))
    maximum=max(skill)
    result=count(skill,maximum)
    final.append(result)
for i,j in enumerate(final):
    print('Case #{}: {}'.format(i+1,j))