import sys

def FilterForm(classname):
    return getattr(sys.modules[__name__], classname+"FilterForm")