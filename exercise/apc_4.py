#question 1
#a
print(list(map(lambda x:x**2,[1,2,3,4,5,6,7,8,9,10])))

#1
#b
print(list(map(lambda x:x**2, [x for x in range(1,21)])))

#2

print("")
print(list(filter(lambda x: x%2==0,[x for x in range(0,11)])))
print(list(filter(lambda x: x%2==0,[x for x in range(1,21)])))

#3
print("")
alist=list(filter(lambda x: x%2==0,[x for x in range(1,11)]))
print(list(map(lambda x:x**2,alist)))

blist=list(filter(lambda x: x%2==0,[x for x in range(1,21)]))
print(list(map(lambda x:x**2,blist)))

#4
clist= ["satyam","kapoor","India","wuhoooo"]
print(max(map(len,clist)))

#5
def filter_long_words(words, n):
    return filter(lambda x: len(x) > n, words)

print (list(filter_long_words(['test', 'not', 'this should'], 5)))

#6

def translate(words):
    lexicon = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
    return list(map(lambda x: lexicon[x], words))


if __name__ == "__main__":
    print (translate(["merry", "christmas"]))


#7
##by list comprehension
print(list(map(lambda x:len(x), ['satyam','kapoor','yo'])))

##by_for_loop
alist=['satyam','kap']
newlist=[]
for x in alist:
    newlist.append(len(x))
print(newlist)

##by_list_expression
print([len(x) for x in alist])

#8
