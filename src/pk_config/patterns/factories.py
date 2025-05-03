# -*- coding: utf-8 -*-

import logging
from abc import ABC, abstractmethod

__all__ = [ 'AbstractFactory' ]

# ------------------------------------------------------------------------------

class AbstractFactory(ABC) :
    """
    Fabrique Abstraite
    """

    @classmethod
    def subclasses(cls) :
        subclasses = []

        for sub in cls.__subclasses__() :
            subclasses.append(sub)
            subclasses.extend(sub.subclasses())

        return subclasses


    def __new__(cls, *args, **kwargs) :
        logging.debug(f'__new__: cls: {cls}, args: {args}, kwargs: {kwargs}')

        # recherche d'un candidat dans les sous-classes
        for sub in cls.subclasses() :
            try :
                if args[0] == sub.id_class :
                    instance = super().__new__(sub)
                    return instance
            except (KeyError, IndexError) :
                pass
            
        return super().__new__(cls)


    def __init__(self, *args, **kwargs) :
        logging.debug(f'__init__: args: {args}, kwargs: {kwargs}')
        
    @classmethod
    def get_id_classes(cls) :
        return {sub.id_class : sub for sub in cls.subclasses()}

# ------------------------------------------------------------------------------
