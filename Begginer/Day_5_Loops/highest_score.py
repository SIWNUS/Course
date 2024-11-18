scores = [120, 125, 36, 66, 58, 89, 45]

highest = 0

for score in scores:
    if highest <= score:
        highest = score

print(highest)