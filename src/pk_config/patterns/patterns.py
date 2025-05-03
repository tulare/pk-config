# -*- coding : utf-8 -*-

__all__ = [ 'singleton', 'Borg' ]

# --------------------------------------------------------------------

def singleton(cls) :
    """ singleton class decorator

        @singleton
        class Counter(object) :
            def __init__(self) :
                self.counter = 0
            def inc(self) :
                self.counter += 1
        
    """
    instances = {}

    # closure
    def getinstance(*args, **kwargs) :
        if cls not in instances :
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance

# --------------------------------------------------------------------

class Borg(object) :
    """ Borg with namespaces

        Borg().mind = 'to share with all of us'

        class PrivateBorg(Borg) :
            __namespace__ = 'private'
            def __init__(self) :
                self.mind = 'to share with all in private'
    """
    __namespace__ = ''
    __shared_state = {}
    
    def __new__(cls, *args, **kwargs) :
        self = object.__new__(cls)
        self.__dict__ = cls.__shared_state.setdefault(cls.__namespace__, {})
        return self

# --------------------------------------------------------------------
