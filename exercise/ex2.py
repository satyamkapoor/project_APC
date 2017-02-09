def create_corners(widthfor):
    dash = "-"
    hashval= "#"
    return((hashval+dash*widthfor)*2+hashval+"\n")

def create_central(widthfor):
    spaces = " "
    hashval="|"
    return((hashval+spaces*widthfor)*2+hashval+"\n")

def create_grid(width,height):
    operation_1 = create_corners(width)+create_central(width)*height
    total = operation_1*2+create_corners(width)
    return total
print(create_grid(8,10))


##Leap year
def leapyear(year):
    if year%4!=0:
        return "Not a leap year"
    elif (year%4==0) and (year%100!=0):
        return "Leap year"
    elif (year%100==0) and (year%400!=0):
        return "Not a leap year 2"
    elif year%400==0:
        return "Leap year 4"
    else:
        return "not found"

print(leapyear(2020))

#bla
def blaprint(numb):
    string = ""
    for prin in range(0,numb):
        string = string +  "bla"
    return string

print(blaprint(10))

#####
def print_stars(n):
    string = ""
    for i in range(n):
        string = i * "*" + "\n"
        print(string)

    for j in range(n):
        string = (n - j) * "*" + "\n"
        print(string)

print_stars(6)


def my_division(divident, divisor):
    remainder = divident%divisor
    ctr = 0
    subs = divident-divisor
    for a in range(subs,0,-divisor):
        ctr+=1
    return(ctr,remainder)

#subsequent powers of minus 2
def powersofminnus2(val):
    list2 = [-2]
    for i in range(1,val):
        toadd = list2[i-1]*(-2)
        list2.append(toadd)
    print(list2)

powersofminnus2(5)

###
def avg_of_element_of_list(list2):
    counter_end = len(list2)
    sumi = 0
    for i in range (0,counter_end):
        sumi = sumi + list2[i]
    return sumi/counter_end


list2 = [20,23,87]
print(avg_of_element_of_list(list2))

###
def reverselist(list2):
    counter_end = len(list2)
    newlist2 = []
    #print(counter_end)
    for i in range (counter_end-1, -1 ,-1):
        newlist2.append(list2[i])
    return newlist2

abc = [2,3,4,5,9]
print(reverselist(abc))

##

vl = 9
while vl>0:
    print("k=",vl)
    vl-=1


###
listforsmallest = ['2','4','6']
def smallestnlargest(list1):
    global  smallestvar
    smallestvar= list1[0]
    global listforsmallest
    largestvar = list1[0]
    for i in range(0,len(list1)):
        if(list1[i]<smallestvar):
            smallestvar = list1[i]

        if (list1[i] > largestvar):
            largestvar = list1[i]

    return smallestvar,largestvar
print(smallestnlargest(listforsmallest))


##nestedlongest list
listfornest=[[2,3,4],[2,6],[8,2,3,3,4,3]]
def longestlist(list1):
    largests=0
    list1len = len(list1)
    for l1 in range(0,list1len):
        abc = len(list1[l1])
        if abc > largests:
            largests = abc

    return largests
print(longestlist(listfornest))

## recursion
def recursum(list):
    if len(list)==1:
        return list[0]
    else:
        return list[0] + recursum(list[1:])

listne=[3,4,4,5,]
print(recursum(listne))


def factorial(takein):
    if takein==1:
        return takein
    else:
        return takein *factorial(takein-1)

print(factorial(4))


####gcd
def gcd(a,b):
    if a==b:
        return a
    elif a>b:
        return gcd(b,a-b)
    else:
        return gcd(a,b-a)

print(gcd(18,21))

ll=[3,1,9,2,2,1,8]
def bubblesort(alist):
    for n in range(len(alist)-1, 0, -1):
        for i in range(n):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist

print(bubblesort(ll))
