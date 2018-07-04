"""
Template - Extend a list with another list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
other_list = [0,0,0]
example_list.extend (other_list)
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]
