def bug_check(num1, num2):
    for i in range(num1, num2+1):
        if i == num2:
            print("Got it.")

bug_check(1, 20)

''' The bug in the above code is normal. The issue is the range.
    We know that range function is descibes like this:
    range(start, stop)
    Here, range is start inclusive but stop exclusive.
    That means in our above function, it gives "i" values from 1 to 19 but not twenty.
    So it starts from start value and ends at stop - 1 value.
    To fix our above code, just change 20 to 21.'''

