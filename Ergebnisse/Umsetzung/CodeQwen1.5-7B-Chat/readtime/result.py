from datetime import timedelta

class Result:
    def __init__(self, seconds, wpm):
        self.seconds = seconds
        self.wpm = wpm

    def minutes(self):
        return self.seconds / 60

    def text(self):
        return f"{self.minutes():.2f} minutes"

    def _add_operator_methods(self):
        for op in ['__add__', '__sub__', '__mul__', '__truediv__']:
            setattr(self, op, self._create_method(op))

    def _create_method(self, op):
        def method(other):
            if isinstance(other, Result):
                return Result(getattr(timedelta(seconds=self.seconds), op)(timedelta(seconds=other.seconds)), self.wpm)
            else:
                return NotImplemented
        return method

    def __repr__(self):
        return f"Result(seconds={self.seconds}, wpm={self.wpm})"

    def __str__(self):
        return self.text()