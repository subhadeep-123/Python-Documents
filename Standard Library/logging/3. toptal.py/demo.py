import logging
toto = logging.getLogger("toto")
toto.setLevel(logging.ERROR)
# assert toto.level == logging.NOTSET
# assert toto.getEffectiveLevel() == logging.WARN
print(toto.getEffectiveLevel())
print(toto.level)
