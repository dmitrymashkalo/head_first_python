# Description: Learning to create classes.
# We won't go into the details of classes,
# but will only touch on those aspects that are useful
# for creating the context manager that our web application expects.

class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    def __repr__(self) -> str:
        return str(self.val)

    def increase(self) -> None:
        self.val += self.incr


a = CountFromBy()
print('Object: ', a.val, a.incr)

a.increase()
print('After first incr: ', a.val, a.incr)

a.increase()
print('After second incr: ', a.val, a.incr)

print(a)
