#!/usr/bin/python

class char:
    def __init__(self, value: str) -> None:
        self.value = value[0]

    def __repr__(self) -> str:
        return self.value


class String:
    def __init__(self, size: int, value: str = ""):
        self.size = size
        if value:
            if len(value) > size:
                del self
                raise Exception(f"ERROR: Not enough space allocated for string of length {len(value)}")
            else:
                self.value = list(value)
        else:
            self.value = [""] * self.size

    def __repr__(self) -> str:
        temp: str = ""
        for character in self.value:
            temp = temp.join(character)
        return temp


class uint8:
    def __init__(self, value: int) -> None:
        self.max_value = 2**8 - 1
        if value > self.max_value or value < 0:
            del self
            raise Exception(f"ERROR: Cannot assign value {value} to unsigned 8-bit integer.")
        else:
            self.value = value

    def __repr__(self) -> int:
        return self.value

    def __int__(self) -> int:
        return self.value

    def __add__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __radd__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __sub__(self, other) -> int:
        if self.value - other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value - other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value - other.__int__()

    def __rsub__(self, other) -> int:
        if other.__int__() - self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() - self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() - self.value

    def __mul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __rmul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __truediv__(self, other) -> int:
        if self.value / other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value / other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value / other.__int__()

    def __rtruediv__(self, other) -> int:
        if other.__int__() / self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() / self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() / self.value

    def __mod__(self, other) -> int:
        if self.value % other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value % other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value % other.__int__()

    def __rmod__(self, other) -> int:
        if other.__int__() % self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() % self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() % self.value

    def __floordiv__(self, other) -> int:
        if self.value // other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value // other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value // other.__int__()

    def __rfloordiv__(self, other) -> int:
        if other.__int__() // self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() // self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() // self.value

    def __pow__(self, other) -> int:
        if self.value ** other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value ** other.__int__() < 0:
            raise Exception("ERROR: Overflow detected")

        return self.value ** other.__int__()

    def __rpow__(self, other) -> int:
        if other.__int__() ** self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() ** self.value < 0:
            raise Exception("ERROR: Overflow detected")

        return other.__int__() ** self.value


class uint16:
    def __init__(self, value: int) -> None:
        if value > 2 ** 16 - 1 or value < 0:
            del self
            Exception(f"ERROR: Cannot assign value {value} to unsigned 16-bit integer.")
        else:
            self.value = value

    def __repr__(self) -> int:
        return self.value

    def __int__(self) -> int:
        return self.value

    def __add__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __radd__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __sub__(self, other) -> int:
        if self.value - other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value - other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value - other.__int__()

    def __rsub__(self, other) -> int:
        if other.__int__() - self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() - self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() - self.value

    def __mul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __rmul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __truediv__(self, other) -> int:
        if self.value / other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value / other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value / other.__int__()

    def __rtruediv__(self, other) -> int:
        if other.__int__() / self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() / self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() / self.value

    def __mod__(self, other) -> int:
        if self.value % other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value % other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value % other.__int__()

    def __rmod__(self, other) -> int:
        if other.__int__() % self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() % self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() % self.value

    def __floordiv__(self, other) -> int:
        if self.value // other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value // other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value // other.__int__()

    def __rfloordiv__(self, other) -> int:
        if other.__int__() // self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() // self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() // self.value

    def __pow__(self, other) -> int:
        if self.value ** other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value ** other.__int__() < 0:
            raise Exception("ERROR: Overflow detected")

        return self.value ** other.__int__()

    def __rpow__(self, other) -> int:
        if other.__int__() ** self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() ** self.value < 0:
            raise Exception("ERROR: Overflow detected")

        return other.__int__() ** self.value


class uint32:
    def __init__(self, value: int) -> None:
        self.max_value = 2**32 - 1
        if value > self.max_value or value < 0:
            del self
            Exception(f"ERROR: Cannot assign value {value} to unsigned 32-bit integer.")
        else:
            self.value = value

    def __repr__(self) -> str:
        return f"{self.value}"

    def __int__(self) -> int:
        return self.value

    def __add__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __radd__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __sub__(self, other) -> int:
        if self.value - other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value - other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value - other.__int__()

    def __rsub__(self, other) -> int:
        if other.__int__() - self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() - self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() - self.value

    def __mul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __rmul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __truediv__(self, other) -> int:
        if self.value / other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value / other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value / other.__int__()

    def __rtruediv__(self, other) -> int:
        if other.__int__() / self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() / self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() / self.value

    def __mod__(self, other) -> int:
        if self.value % other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value % other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value % other.__int__()

    def __rmod__(self, other) -> int:
        if other.__int__() % self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() % self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() % self.value

    def __floordiv__(self, other) -> int:
        if self.value // other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value // other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value // other.__int__()

    def __rfloordiv__(self, other) -> int:
        if other.__int__() // self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() // self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() // self.value

    def __pow__(self, other) -> int:
        if self.value ** other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value ** other.__int__() < 0:
            raise Exception("ERROR: Overflow detected")

        return self.value ** other.__int__()

    def __rpow__(self, other) -> int:
        if other.__int__() ** self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() ** self.value < 0:
            raise Exception("ERROR: Overflow detected")

        return other.__int__() ** self.value


class uint64:
    def __init__(self, value: int) -> None:
        self.max_value = 2**64 - 1
        if value > 2 ** 64 - 1 or value < 0:
            del self
            Exception(f"ERROR: Cannot assign value {value} to unsigned 64-bit integer.")
        else:
            self.value = value

    def __repr__(self) -> str:
        return f"{self.value}"

    def __int__(self) -> int:
        return self.value

    def __add__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __radd__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __sub__(self, other) -> int:
        if self.value - other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value - other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value - other.__int__()

    def __rsub__(self, other) -> int:
        if other.__int__() - self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() - self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() - self.value

    def __mul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __rmul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __truediv__(self, other) -> int:
        if self.value / other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value / other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value / other.__int__()

    def __rtruediv__(self, other) -> int:
        if other.__int__() / self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() / self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() / self.value

    def __mod__(self, other) -> int:
        if self.value % other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value % other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value % other.__int__()

    def __rmod__(self, other) -> int:
        if other.__int__() % self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() % self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() % self.value

    def __floordiv__(self, other) -> int:
        if self.value // other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value // other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value // other.__int__()

    def __rfloordiv__(self, other) -> int:
        if other.__int__() // self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() // self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() // self.value

    def __pow__(self, other) -> int:
        if self.value ** other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value ** other.__int__() < 0:
            raise Exception("ERROR: Overflow detected")

        return self.value ** other.__int__()

    def __rpow__(self, other) -> int:
        if other.__int__() ** self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() ** self.value < 0:
            raise Exception("ERROR: Overflow detected")

        return other.__int__() ** self.value

class uint128:
    def __init__(self, value: int) -> None:
        self.max_value = 2**128 - 1
        if value > 2 ** 64 - 1 or value < 0:
            del self
            Exception(f"ERROR: Cannot assign value {value} to unsigned 128-bit integer.")
        else:
            self.value = value

    def __repr__(self) -> str:
        return f"{self.value}"

    def __int__(self) -> int:
        return self.value

    def __add__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __radd__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __sub__(self, other) -> int:
        if self.value - other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value - other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value - other.__int__()

    def __rsub__(self, other) -> int:
        if other.__int__() - self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() - self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() - self.value

    def __mul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __rmul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __truediv__(self, other) -> int:
        if self.value / other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value / other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value / other.__int__()

    def __rtruediv__(self, other) -> int:
        if other.__int__() / self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() / self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() / self.value

    def __mod__(self, other) -> int:
        if self.value % other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value % other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value % other.__int__()

    def __rmod__(self, other) -> int:
        if other.__int__() % self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() % self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() % self.value

    def __floordiv__(self, other) -> int:
        if self.value // other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value // other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value // other.__int__()

    def __rfloordiv__(self, other) -> int:
        if other.__int__() // self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() // self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() // self.value

    def __pow__(self, other) -> int:
        if self.value ** other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value ** other.__int__() < 0:
            raise Exception("ERROR: Overflow detected")

        return self.value ** other.__int__()

    def __rpow__(self, other) -> int:
        if other.__int__() ** self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() ** self.value < 0:
            raise Exception("ERROR: Overflow detected")

        return other.__int__() ** self.value


class uintarb:
    def __init__(self, value: int, bits: int) -> None:
        self.max_value = 2**bits - 1
        if value > self.max_value or value < 0:
            del self
            Exception(f"ERROR: Cannot assign value {value} to unsigned {bits}-bit integer.")
        else:
            self.value = value

    def __repr__(self) -> str:
        return f"{self.value}"

    def __int__(self) -> int:
        return self.value

    def __add__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __radd__(self, other) -> int:
        if self.value + other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value + other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value + other.__int__()

    def __sub__(self, other) -> int:
        if self.value - other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value - other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value - other.__int__()

    def __rsub__(self, other) -> int:
        if other.__int__() - self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() - self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() - self.value

    def __mul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __rmul__(self, other) -> int:
        if self.value * other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value * other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value * other.__int__()

    def __truediv__(self, other) -> int:
        if self.value / other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value / other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value / other.__int__()

    def __rtruediv__(self, other) -> int:
        if other.__int__() / self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() / self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() / self.value

    def __mod__(self, other) -> int:
        if self.value % other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value % other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value % other.__int__()

    def __rmod__(self, other) -> int:
        if other.__int__() % self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() % self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() % self.value

    def __floordiv__(self, other) -> int:
        if self.value // other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value // other.__int__() < 0:
            raise Exception("ERROR: Underflow detected")

        return self.value // other.__int__()

    def __rfloordiv__(self, other) -> int:
        if other.__int__() // self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() // self.value < 0:
            raise Exception("ERROR: Underflow detected")

        return other.__int__() // self.value

    def __pow__(self, other) -> int:
        if self.value ** other.__int__() > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif self.value ** other.__int__() < 0:
            raise Exception("ERROR: Overflow detected")

        return self.value ** other.__int__()

    def __rpow__(self, other) -> int:
        if other.__int__() ** self.value > self.max_value:
            raise Exception("ERROR: Overflow detected")
        elif other.__int__() ** self.value < 0:
            raise Exception("ERROR: Overflow detected")

        return other.__int__() ** self.value
