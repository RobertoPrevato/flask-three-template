
class ObjDict(dict):
    """
    Derived dictionary class, that allows to access dictionary items as object attributes.
    http://goodcode.io/articles/python-dict-object/
    """
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("Key not found: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("Key not found: " + name)
