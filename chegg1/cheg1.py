#reading a file
lines =  [line.strip().split() for line in open("runners.txt")]
#printing file
print(lines)
#splitting contents

#printing first names
[print(x[0]) for x in lines]

print(filt(lambda x: x>2, lines))


