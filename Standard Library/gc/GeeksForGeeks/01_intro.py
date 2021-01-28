import gc
val = list(range(10))
del val
collected = gc.collect()
print(f"Garbage collector: collected {collected} objects")
