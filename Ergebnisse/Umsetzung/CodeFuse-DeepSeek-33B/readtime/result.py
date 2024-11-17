from datetime import timedelta

class Result:
    """
    Represents the estimated reading time for a given content.

    Attributes:
    seconds (int): The total number of seconds in the delta.
    wpm (int): The words per minute rate used for the calculation.
    """

    def __init__(self, seconds, wpm):
        """
        Initialize the Result object.

        Parameters:
        seconds (int): The total number of seconds in the delta.
        wpm (int): The words per minute rate used for the calculation.
        """
        self.seconds = seconds
        self.wpm = wpm

    def minutes(self):
        """
        Calculate the estimated reading time in minutes.

        Returns:
        float: The estimated reading time in minutes.
        """
        return self.seconds / 60.0

    def text(self):
        """
        Get the text representation of the read time.

        Returns:
        str: The text representation of the read time.
        """
        delta = timedelta(seconds=self.seconds)
        return str(delta)

    def _add_operator_methods(self):
        """
        Add operator methods to the class dynamically.
        """
        def __add__(self, other):
            return Result(self.seconds + other.seconds, self.wpm)

        def __sub__(self, other):
            return Result(self.seconds - other.seconds, self.wpm)

        def __mul__(self, other):
            return Result(self.seconds * other, self.wpm)

        def __rmul__(self, other):
            return self.__mul__(other)

        def __truediv__(self, other):
            return Result(self.seconds / other, self.wpm)

        def __floordiv__(self, other):
            return Result(self.seconds // other, self.wpm)

        def __mod__(self, other):
            return Result(self.seconds % other, self.wpm)

        def __divmod__(self, other):
            return Result(self.seconds // other, self.wpm), Result(self.seconds % other, self.wpm)

        def __pow__(self, other):
            return Result(self.seconds ** other, self.wpm)

        def __rpow__(self, other):
            return self.__pow__(other)

        def __neg__(self):
            return Result(-self.seconds, self.wpm)

        def __pos__(self):
            return Result(+self.seconds, self.wpm)

        def __abs__(self):
            return Result(abs(self.seconds), self.wpm)

        def __lt__(self, other):
            return self.seconds < other.seconds

        def __le__(self, other):
            return self.seconds <= other.seconds

        def __eq__(self, other):
            return self.seconds == other.seconds

        def __ne__(self, other):
            return self.seconds != other.seconds

        def __gt__(self, other):
            return self.seconds > other.seconds

        def __ge__(self, other):
            return self.seconds >= other.seconds

        self.__add__ = __add__
        self.__sub__ = __sub__
        self.__mul__ = __mul__
        self.__rmul__ = __rmul__
        self.__truediv__ = __truediv__
        self.__floordiv__ = __floordiv__
        self.__mod__ = __mod__
        self.__divmod__ = __divmod__
        self.__pow__ = __pow__
        self.__rpow__ = __rpow__
        self.__neg__ = __neg__
        self.__pos__ = __pos__
        self.__abs__ = __abs__
        self.__lt__ = __lt__
        self.__le__ = __le__
        self.__eq__ = __eq__
        self.__ne__ = __ne__
        self.__gt__ = __gt__
        self.__ge__ = __ge__

    def _create_method(self, op):
        """
        Create a method for the Result class based on the given operation.

        Parameters:
        op (str): The operation to create the method for.
        """
        def method(self, other):
            return Result(eval(f"self.seconds {op} other.seconds"), self.wpm)

        setattr(Result, f"__{op}__", method)

    _add_operator_methods()
    _create_method("+")
    _create_method("-")
    _create_method("*")
    _create_method("/")
    _create_method("//")
    _create_method("%")
    _create_method("**")