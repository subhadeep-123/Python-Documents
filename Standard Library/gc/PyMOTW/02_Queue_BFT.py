import gc
import pprint
import queue


class Graph(object):
    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        print("Linking nodes {self}.next = {next}")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"


# Construct a graph cycle
one = Graph('one')
two = Graph('two')
three = Graph('three')
one.set_next(two)
two.set_next(three)
three.set_next(one)

print()

seen = set()
to_process = queue.Queue()

to_process.put(([], three))

# Look for cycles, building the object chain for each object we find
# in the queue so we can print the full cycle when we're done.
while not to_process.empty():
    chain, next = to_process.get()
    chain = chain[:]
    chain.append(next)
    print('Examining:', repr(next))
    seen.add(id(next))
    for r in gc.get_referents(next):
        if isinstance(r, basestring) or isinstance(r, type):
            # Ignore strings and classes
            pass
        elif id(r) in seen:
            print()
            print('Found a cycle to %s:' % r)
            for i, link in enumerate(chain):
                print('  %d: ' % i)
                pprint.pprint(link)
        else:
            to_process.put((chain, r))
