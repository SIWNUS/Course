def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    """ This function gives a leap year check.
        Here is hoe it goes:
        -> year divisible by 4
        -> not divisible by 100
        -> but divisible by 400 """
    if year % 4 == 0 and not year % 100 == 0:
        return True
    elif year % 100 == 0 and not year % 400 == 0:
        return False
    elif year % 400 == 0:
        return True
    else:
        return False
        
y = int(input())
leap_year = is_leap_year(y)
print(leap_year)
