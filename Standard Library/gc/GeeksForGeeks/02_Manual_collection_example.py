import gc


def create_cycle():
    x = {}
    x[i+1] = x
    print(x)


collected = gc.collect()
print(f"Garbage collector: collected {collected} objects")

print("Creating cycles..")
for i in range(10):
    create_cycle()

collected = gc.collect()
print(f"Garbage collector: collected {collected} objects")
