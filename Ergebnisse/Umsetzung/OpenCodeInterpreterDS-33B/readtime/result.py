class Result:
    def __init__(self, seconds, wpm):
        self.seconds = seconds
        self.wpm = wpm
        self._add_operator_methods()

    def seconds(self):
        return self.seconds

    def minutes(self):
        return self.seconds / 60

    def text(self):
        return f"{self.minutes()} minutes"

    def _add_operator_methods(self):
        self.__add__ = self._create_method('add')
        self.__sub__ = self._create_method('sub')
        self.__mul__ = self._create_method('mul')
        self.__truediv__ = self._create_method('truediv')

    def _create_method(self, op):
        def method(other):
            if isinstance(other, Result):
                other = other.seconds
            return Result(eval(f"self.seconds {op} other"), self.wpm)
        return method