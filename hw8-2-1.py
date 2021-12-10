# Author: Nolan (AMDG) 1/9/2021

def count_odds(numbs):
    odd = 0
    for x in numbs:
        if x % 2 != 0:
            odd += 1
    return odd

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)
