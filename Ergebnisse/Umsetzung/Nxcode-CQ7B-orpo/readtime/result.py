from datetime import timedelta

class Result(timedelta):
    def __init__(self, seconds, wpm):
        super().__init__(seconds=seconds)
        self.wpm = wpm

    def seconds(self):
        return self.total_seconds()

    def minutes(self):
        return self.total_seconds() / 60

    def text(self):
        return f"{self.minutes():.2f} minutes"

    def _add_operator_methods(self):
        for op in ['__add__', '__sub__', '__mul__', '__truediv__']:
            setattr(self, op, self._create_method(op))

    def _create_method(self, op):
        def method(other):
            if isinstance(other, timedelta):
                return super()._create_method(op)(other)
            else:
                return super()._create_method(op)(Result(other, self.wpm))
        return method

    def __repr__(self):
        return f"Result({self.minutes():.2f} minutes)"