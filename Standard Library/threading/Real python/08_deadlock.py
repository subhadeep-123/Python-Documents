"""
Before you move on, you should lock at a common plroblem when usings Locks.
As we saw, if the Lock has already been acquired, a second call to .acquire()
will wait until the thread that is holding the Lock calls .release().
"""
import threading


def lock():
    l = threading.Lock()
    print("Before first acquire")
    l.acquire()
    print("Before second acquire")
    # l.release() #It is the soln
    l.acquire()
    print("Acquired lock twice")
    l.release()
    l.release()


def rlock():
    l = threading.RLock()
    print("Before first acquire")
    l.acquire()
    print("Before second acquire")
    l.acquire()
    print("Acquired lock twice")
    l.release()
    l.release()


# def cmlock():
#     with threading.Lock() as l:
#         print("Before first acquire")
#         l.acquire()
#         print("Before second acquire")
#         l.acquire()
#         print("Acquired lock twice")
# cmlock()
"""
A Deadlock happens from one of the two subtle things:
1. An Implementation bug where a Lock is not released properly
2. A design issue where a utility function needs to be called by functions
that might or might not already have the Lock.

For the first situation we can use contaxtmanager whenever possible,
as they helo to avoid situations where an exception skips you over the lock
.release() call.

Thankfully, Python threading has a second object, called RLock, that is designed 
for just this situation. It allows a thread to .acquire() an RLock multiple times 
before it calls .release(). That thread is still required to call .release() the 
same number of times it called .acquire(), but it should be doing that anyway.

Lock and Rlock are two fo the basic tools used in threaded programming to prevent
race conditions. THere are a few other that work in different ways. 
"""
