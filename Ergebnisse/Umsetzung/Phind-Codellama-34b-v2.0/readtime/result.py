class Result:
    def __init__(self, seconds):
        self.seconds = seconds

    def minutes(self):
        return self.seconds / 60

    def text(self):
        return f"{self.minutes():.2f} minutes"

    def __str__(self):
        return self.text()

    def __add__(self, other):
        return Result(self.seconds + other.seconds)

    def __sub__(self, other):
        return Result(self.seconds - other.seconds)

    def __mul__(self, other):
        return Result(self.seconds * other.seconds)

    def __truediv__(self, other):
        return Result(self.seconds / other.seconds)
