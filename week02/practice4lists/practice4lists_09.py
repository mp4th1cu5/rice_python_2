"""
Template - Compute the largest number in a list
"""

def list_max(numbers):
    """
    Given a list of numbers, return the maximum (largest) number
    in the list
    """
    num = 0
    for number in numbers:
        if number > num:
            num = number
        else:
            continue
    return num

# Tests
print(list_max([4]))
print(list_max([-3, 4]))
print(list_max([5, 3, 1, 7, -3, -4]))
print(list_max([1, 2, 3, 4, 5]))


# Output
#4
#4
#7
#5
