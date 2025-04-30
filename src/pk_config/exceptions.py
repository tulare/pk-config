# -*- coding: utf-8 -*-

__all__ = [
    'ConfigurationError', 'ConfigurationKeyError',
    'RegistryException',
    'RegistryKeyOk', 'RegistryKeyError',
    'RegistryValueError',
]

# --------------------------------------------------------------------

class ConfigurationError(BaseException) :
    pass

class ConfigurationKeyError(BaseException) :
    pass

# --------------------------------------------------------------------

class RegistryException(BaseException) :
    pass

class RegistryKeyOk(RegistryException) :
    pass

class RegistryKeyError(RegistryException) :
    pass

class RegistryValueError(RegistryException) :
    pass

# --------------------------------------------------------------------
