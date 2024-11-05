import math

class ScientificCalculator:

    def user_input(self, x):
        try:
            return float(x)
        except ( ValueError, TypeError):
            raise ValueError("user input must be a number")

    def sin(self, x):
        return math.sin(math.radians(x))

    def cos(self, x):
        return math.cos(math.radians(x))

    def tan(self, x):
        return math.tan(math.radians(x))

    def sqrt(self, x):
        return math.sqrt(x)

    def log(self, x):
        return math.log(x)

    def exp(self, x):
        return math.exp(x)