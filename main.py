# Task1:ListComprehensions
square_list = [n**2 for n in range(1, 11)]
print(square_list)


# Task2: Functions
def square_in_range(i, j):
    return [n ** 2 for n in range(i, j)]


print(square_in_range(1, 15))

