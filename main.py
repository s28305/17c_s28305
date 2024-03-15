import math

# Task1:ListComprehensions
square_list = [n**2 for n in range(1, 11)]
print(square_list)


# Task2: Functions
def e_squares(start, end):
    return [n ** 2 for n in range(start, end)]


print(e_squares(1, 15))


# Task3: Classes
class SquareGenerator:
    def __init__(self, start, end):
        self.square_list = [n ** 2 for n in range(start, end)]


x = SquareGenerator(1, 15)
print(x.square_list)


# Task4: Libraries
def e_roots(num_list):
    return [math.sqrt(n) for n in num_list]


print(e_roots(x.square_list))


# Task5: Exceptions
class SquareGenerator:
    def __init__(self, start, end):
        if (start <= end):
            self.square_list = [n ** 2 for n in range(start, end)]
        else:
            print("Invalid values inserted")


x = SquareGenerator(21, 15)
