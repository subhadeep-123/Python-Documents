# Multithreaded Programming
Running several threads is similar to running several different programs concurrently, but with the following benefits −

* Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.

* Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.

A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.

* It can be pre-empted (interrupted).

* It can temporarily be put on hold (also known as sleeping) while other threads are running - this is called yielding.

There are two different kind of threads −

* kernel thread
* user thread
  
Kernel Threads are a part of the operating system, while the User-space threads are not implemented in the kernel.

There are two modules which support the usage of threads in Python3 −
* _thread
* threading


## The Threading Module
The newer threading module included with Python 2.4 provides much more powerful, high-level support for threads than the thread module discussed in the previous section.

The threading module exposes all the methods of the thread module and provides some additional methods −
* **threading.activeCount()** - Returns the number of thread objects that are active.
*  **threading.currentThread()** - Returns the number of thread objects in the caller's thread control.
*  **threading.enumerate()** - Returns a list of all thread objects that are currently active.

In addition to the methods, the threading module has the Thread class that implements threading. The methods provided by the Thread class are as follows −
* **run**() - The run() method is the entry point for a thread.
* **start**() - The start() method starts a thread by calling the run method.
* **join**([time]) - The join() waits for threads to terminate.
* **isAlive**() - the isAlive() method checks whether a thread is still executing.
* **getName**() - The getName() method returns the name of a thread.
* **setName**() - The setName() methods set the name of a thread.