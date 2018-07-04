"""
Template - Append several item to a list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
for i in range (3):
    example_list.append(0)
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]
