"""
Design a base structural class `Vehicle` containing a method `describe()`. Derive a subclass `ElectricCar`
that utilizes `super().__init__()` to inherit structural configurations from the parent class, while providing a
specialized `describe()` function override that prints out internal battery metrics as well.
Sample Input: ecar = ElectricCar('Tesla', 'Model 3', range=350); ecar.describe()
Expected Output: 'Tesla Model 3 with a 350-mile electric battery range profile.'
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        print(f"{self.brand} {self.model}")


class ElectricCar(Vehicle):
    def __init__(self, brand, model, range):
        super().__init__(brand, model)
        self.range = range

    def describe(self):
        print(f"{self.brand} {self.model} with a {self.range}-mile electric battery range profile.")


# Sample Input
ecar = ElectricCar("Tesla", "Model 3", 350)
ecar.describe()