A logger is unique by name, meaning that if a logger with the name “toto” has been created, the consequent calls of logging.getLogger("toto") will return the same object:

As you might have guessed, loggers have a hierarchy. On top of the hierarchy is the root logger, which can be accessed via logging.root. This logger is called when methods like logging.debug() is used. By default, the root log level is WARN, so every log with lower level (for example via logging.info("info")) will be ignored. Another particularity of the root logger is that its default handler will be created the first time a log with a level greater than WARN is logged. Using the root logger directly or indirectly via methods like logging.debug() is generally not recommended.

By default, when a new logger is created, its parent will be set to the root logger:

```
lab = logging.getLogger("a.b")
assert lab.parent == logging.root # lab's parent is indeed the root logger
```

However, the logger uses the “dot notation,” meaning that a logger with the name “a.b” will be the child of the logger “a.” However, this is only true if the logger “a” has been created, otherwise “ab” parent is still the root.

```
la = logging.getLogger("a")
assert lab.parent == la # lab's parent is now la instead of root
```

When a logger decides whether a log should pass according to the level check (e.g., if the log level is lower than logger level, the log will be ignored), it uses its “effective level” instead of the actual level. The effective level is the same as logger level if the level is not NOTSET, i.e., all the values from DEBUG up to CRITICAL; however, if the logger level is NOTSET, then the effective level will be the first ancestor level that has a non-NOTSET level.

By default, a new logger has the NOTSET level, and as the root logger has a WARN level, the logger’s effective level will be WARN. So even if a new logger has some handlers attached, these handlers will not be called unless the log level exceeds WARN:
```
toto_logger = logging.getLogger("toto")
assert toto_logger.level == logging.NOTSET # new logger has NOTSET level
assert toto_logger.getEffectiveLevel() == logging.WARN # and its effective level is the root logger level, i.e. WARN

# attach a console handler to toto_logger
console_handler = logging.StreamHandler()
toto_logger.addHandler(console_handler)
toto_logger.debug("debug") # nothing is displayed as the log level DEBUG is smaller than toto effective level
toto_logger.setLevel(logging.DEBUG)
toto_logger.debug("debug message") # now you should see "debug message" on screen
```

By default, the logger level will be used to decide of the a log passes: If the log level is lower than logger level, the log will be ignored.

## Python Logging Best Pratices

The logging module is indeed very handy, but it contains some quirks that can cause long hours of headache for even the best Python developers. Here are the best practices for using this module in my opinion:

* Configure the root logger but never use it in your code—e.g., never call a function like logging.info(), which actually calls the root logger behind the scene. If you want to catch error messages from libraries you use, make sure to configure the root logger to write to a file, for example, to make the debugging easier. By default, the root logger only outputs to stderr, so the log can get lost easily.
* To use the logging, make sure to create a new logger by using logging.getLogger(logger name). I usually use __name__ as the logger name, but anything can be used, as long as it is consistent. To add more handlers, I usually have a method that returns a logger (you can find the gist on https://gist.github.com/nguyenkims/e92df0f8bd49973f0c94bddf36ed7fd0).

```
Refer to - app.py
```

* Use RotatingFileHandler classes, such as the TimedRotatingFileHandler used in the example instead of FileHandler, as it will rotate the file for you automatically when the file reaches a size limit or do it everyday.
* Use tools like Sentry, Airbrake, Raygun, etc., to catch error logs automatically for you. This is especially useful in the context of a web app, where the log can be very verbose and error logs can get lost easily. Another advantage of using these tools is that you can get details about variable values in the error so you can know what URL triggers the error, which user is concerned, etc.
