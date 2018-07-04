"""
Template - Remove duplicates from a list while preserving the order of items
"""

myList = [1, 2, 3, 1, 2, 5, 6, 7, 8]
cleanlist = []
[cleanlist.append(x) for x in myList if x not in cleanlist]


def remove_duplicates(items):
    """
    Given a list, return a list with duplicate items removed
    and the remaining items in the same order
    """
    cleanlist = []
    for item in items:
        if item not in cleanlist:
            cleanlist.append(item)
    return cleanlist



# Test code
print(remove_duplicates([]))
print(remove_duplicates([1, 2, 3, 4]))"""
Template - Flatten a nested list
"""

def flatten(nested_list):
    """
    Given a list whose items are list,
    return the list formed by joining all of these lists
    """
    flat_list=[]
    for element in nested_list:
        flat_list.extend(element)
    return flat_list


# Test code
print(flatten([]))
print(flatten([[]]))
print(flatten([[1, 2, 3]]))
print(flatten([["cat", "dog"], ["pig", "cow"]]))
print(flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))


# Output
#[]
#[]
#[1, 2, 3]
#['cat', 'dog', 'pig', 'cow']
#[9, 8, 7, 6, 5, 4, 3, 2, 1]

print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 6, 6]))
print(remove_duplicates(["cat", "dog", "cat", "pig", "cow", "cat", "pig", "pug"]))


# Output
#[]
#[1, 2, 3, 4]
#[1, 2, 3, 4, 5, 6]
#['cat', 'dog', 'pig', 'cow', 'pug']
