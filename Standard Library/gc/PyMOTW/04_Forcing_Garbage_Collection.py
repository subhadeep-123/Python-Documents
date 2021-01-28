import gc
import pprint


class Graph(object):
    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        print(f"Linking nodes {self}.next = {next}")
        self.next = next

    def __repr__(self):
        return f"{self.__class__.__name__}, {self.name}"

    def __del__(self):
        print(f"{self}.__del__()")


# Construct a graph cycle
one = Graph('one')
two = Graph('two')
three = Graph('three')
one.set_next(two)
two.set_next(three)
three.set_next(one)


print()
one = two = three = None

# Show effect of garbage collection
for i in range(2):
    print(f"Collecting {i}....")
    n = gc.collect()
    print(f"Uncechable objects {n}")
    print("Remaining Garbage:")
    pprint.pprint(gc.garbage)
    print()
