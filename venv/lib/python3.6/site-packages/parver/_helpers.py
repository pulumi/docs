# coding: utf-8
from __future__ import absolute_import, division, print_function

from collections import deque

import six
from six.moves.collections_abc import Iterable


class UnsetType(object):
    def __repr__(self):
        return 'UNSET'


UNSET = UnsetType()
del UnsetType


class Infinity(object):

    def __repr__(self):
        return "Infinity"

    def __hash__(self):
        return hash(repr(self))

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        return not isinstance(other, self.__class__)

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True

    def __neg__(self):
        return NegativeInfinity


Infinity = Infinity()


class NegativeInfinity(object):

    def __repr__(self):
        return "-Infinity"

    def __hash__(self):
        return hash(repr(self))

    def __lt__(self, other):
        return True

    def __le__(self, other):
        return True

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        return not isinstance(other, self.__class__)

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        return False

    def __neg__(self):
        return Infinity


NegativeInfinity = NegativeInfinity()


def fixup_module_metadata(module_name, namespace):
    def fix_one(obj):
        mod = getattr(obj, '__module__', None)
        if mod is not None and mod.startswith('parver.'):
            obj.__module__ = module_name
            if isinstance(obj, type):
                for attr_value in obj.__dict__.values():
                    fix_one(attr_value)

    for objname in namespace['__all__']:
        obj = namespace[objname]
        fix_one(obj)


def force_tuple(n):
    if isinstance(n, six.string_types):
        raise TypeError('Expected an iterable or int.')
    if not isinstance(n, Iterable):
        return n,
    if not isinstance(n, tuple):
        return tuple(n)
    return n


def force_lower(s):
    # We only do this if it's a string, otherwise we let the wrong type pass
    # through and let the validator complain.
    if isinstance(s, str):
        return s.lower()
    return s


def doc_signature(signature):
    def decorator(fn):
        fn.__parverdoc_signature__ = signature
        return fn
    return decorator


def kwonly_args(kws, required, withdefaults=(), leftovers=False):
    """
    Based on the snippet by Eric Snow
    http://code.activestate.com/recipes/577940

    SPDX-License-Identifier: MIT
    """

    if hasattr(withdefaults, 'items'):
        # allows for OrderedDict to be passed
        withdefaults = withdefaults.items()

    kwonly = []

    # extract the required keyword-only arguments
    missing = []
    for name in required:
        if name not in kws:
            missing.append(name)
        else:
            kwonly.append(kws.pop(name))

    # validate required keyword-only arguments
    if missing:
        if len(missing) > 2:
            end = 's: %s, and %s' % (', '.join(missing[:-1]), missing[-1])
        elif len(missing) == 2:
            end = 's: %s and %s' % tuple(missing)
        else:
            end = ': %s' % tuple(missing)

        msg = 'missing %s required keyword-only argument%s'
        raise TypeError(msg % (len(missing), end))

    # handle the withdefaults
    for name, value in withdefaults:
        if name not in kws:
            kwonly.append(value)
        else:
            kwonly.append(kws.pop(name))

    # handle any leftovers
    if not leftovers and kws:
        msg = "got an unexpected keyword argument '%s'"
        raise TypeError(msg % (kws.keys()[0]))

    return [kws] + kwonly


def last(iterable, **kwargs):
    _, default = kwonly_args(kwargs, (), dict(default=UNSET))

    try:
        return deque(iterable, maxlen=1).pop()
    except IndexError:
        if default is UNSET:
            raise
        return default


IMPLICIT_ZERO = ''
