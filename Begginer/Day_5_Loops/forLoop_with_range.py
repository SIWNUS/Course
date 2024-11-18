#for number in range(a, b, step)
#  print(number)

# a is the start and it iterates till it reaches b but stops there and does not include b
# default step size is 1. i.e: it increses the count by 1.

# if a is 3 and b is 9, it prints 3, 4, 5, 6, 7, 8.
# But if you specify the step size to be 3, it prints 3, 6.

# As you can see it doesn't print 9 because the loop terminates when it reaches 9.
# If you want it to print 9 then set your b as 10.


# Gauss Problem: Add all numbers from 1 to 100.

ans = 0
for num in range(1, 101):
    ans += num

print(ans)