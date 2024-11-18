flist = []
for f in range(3, 101, 3):
    flist.append(f)

print(flist)

blist = []
for b in range(5, 101, 5):
    blist.append(b)

print(blist)

fblist = []
for f in flist:
    for b in blist:
        if f == b:
            fblist.append(f)

print(fblist)

for number in range(1, 101):
    if number in fblist:
        number = "FizzBuzz"
    elif number in flist:
        number = "Fizz"
    elif number in blist:
        number = "Buzz"
        
    print(number)


