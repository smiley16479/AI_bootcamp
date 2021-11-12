You can reload a module when it has already been imported by using importlib.reload():

from importlib import reload  # Python 3.4+
import foo
(...)
if is_changed(foo):
    foo = reload(foo)

#Usefull link:

##Python Module Attributes: name, doc, file, dict:
https://www.tutorialsteacher.com/python/python-module-attributes

##Opérations usuelles sur des chaînes:
https://docs.python.org/fr/3.5/library/string.html

##Generator:
https://wiki.python.org/moin/Generators