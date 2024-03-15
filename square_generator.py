class SquareGenerator:
    def __init__(self, start, end):
        if (start <= end):
            self.square_list = [n ** 2 for n in range(start, end)]
        else:
            print("Invalid values inserted")