# Task 6: Modules
class SquareGenerator:
    def __init__(self, start, end):
        if start <= end:
            self.square_list = [n ** 2 for n in range(start, end)]
        else:
            raise ValueError("Invalid values inserted")


# Task8:Inheritance
class CubicGenerator(SquareGenerator):
    def __init__(self, start, end):
        super().__init__(start, end)
        if start <= end:
            self.cube_list = [n ** 3 for n in range(start, end)]
        else:
            raise ValueError("Invalid values inserted")


square_x = SquareGenerator(1, 11)
print("Squares:", square_x.square_list)

cubic_x = CubicGenerator(1, 11)
print("Cubes:", cubic_x.cube_list)
