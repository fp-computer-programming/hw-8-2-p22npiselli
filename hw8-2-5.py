# Author: Nolan (AMDG) 1/9/2021

def sum_before_odd(numbs):
    sum = 0
    for x in numbs:
        if x % 2 != 0:
            break
        else:
            sum += x
    return sum

print(sum_before_odd([2, 4, 6, 8, 9]) == 20)
print(sum_before_odd([13, 12, 10]) == 0)
print(sum_before_odd([14, 16, 32]) == 62)