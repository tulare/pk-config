# -*- coding: utf-8 -*-

import logging
from abc import ABC, abstractmethod

__all__ = [ 'IObserver', 'IObservable', 'Observable' ]

# --- INTERFACES -----------------------------------------------

class IObserver(ABC) :

    @abstractmethod
    def observe(self, *args, **kwargs) :
        pass
# ---

class IObservable(ABC) :
    
    @abstractmethod
    def add_observer(self, observer) :
        pass

    @abstractmethod
    def remove_observer(self, observer) :
        pass

    @abstractmethod
    def remove_all_observers(self) :
        pass

    @abstractmethod
    def notify(self, *args, **kwargs) :
        pass

# --- IMPLEMENTATIONS -------------------------------------------

class Observable(IObservable) :

    def __init__(self) :
        self._observers = set()

    def add_observer(self, observer) :
        if not isinstance(observer, IObserver) :
            raise ValueError(
                "{} : don't respect interface IObserver".format(
                    observer
                )
            )
        self._observers.add(observer)

    def remove_observer(self, observer) :
        self._observers.remove(observer)

    def remove_all_observers(self) :
        self._observers.clear()

    def notify(self, *args, **kwargs) :
        for observer in self._observers :
            observer.observe(*args, **kwargs)
            
