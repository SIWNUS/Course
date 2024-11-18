def is_prime(num):
    if num > 2:
        for i in range(2, num):
            if num%i != 0:
                return True
            else:
                return False
    elif num == 2:
        return True
    else:
        return False

number = int(input())
result = is_prime(number)
print(result)