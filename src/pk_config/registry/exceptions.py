# -*- coding: utf-8 -*-

__all__ = [
    'RegistryException',
    'RegistryKeyOk', 'RegistryKeyError',
    'RegistryValueError',
]


# --------------------------------------------------------------------

class RegistryException(BaseException) :
    pass

# ---

class RegistryKeyOk(RegistryException) :
    pass

# ---

class RegistryKeyError(RegistryException) :
    pass

# ---

class RegistryValueError(RegistryException) :
    pass

# --------------------------------------------------------------------
