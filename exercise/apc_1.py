#question 1
print([abs(x) for x in [1,1,3,5]])

#question2
print([x  for x in [1,-1,2,-5] if x>0])
print(list((map(lambda x: x>0, [1,-2]))))
#gives outputs in True & False

#question3
print([int(str(x).replace("0","-1")) for x in [1,0,3,0]])

#question4
print([x.upper() for x in ["a","b","C"]])

#question5
print([x**2 for x in range(1,11)])

#question6
k = [x for x in [[],[0,1,2],[],[3,6,7,21]] if len(x)>0]
print(k)

#question7
alist = ['Hello','Me']
print([[x,len(x)] for x in alist])

#question8
alist=[120,1,2,100,200]
m=[0 if x%10==0 else x for x in alist]
print(m)

#question 9
list1=['apple','orange']
list2=[2,5,10]
print([(x,y) for x in list1 for y in list2])

#question 10
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print([(list1[x],list2[x]) for x in range(len(list1))])
