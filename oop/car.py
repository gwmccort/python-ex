# car class
# from: https://realpython.com/python3-object-oriented-programming

class Car:

    # class initilizer
    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage

    # convert class instance to string
    def __str__(self):
        return f"Car color: {self.color} has {self.mileage}"


c1 = Car('red', 50000)
c2 = Car('blue', 70000)

for c in (c1, c2):
    print(c)
