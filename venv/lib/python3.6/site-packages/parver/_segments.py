# coding: utf-8
from __future__ import absolute_import, division, print_function

import attr


@attr.s(slots=True)
class Segment(object):
    pass


@attr.s(slots=True)
class V(Segment):
    pass


@attr.s(slots=True)
class ValueSegment(Segment):
    value = attr.ib()


@attr.s(slots=True)
class Epoch(ValueSegment):
    pass


@attr.s(slots=True)
class Release(ValueSegment):
    pass


@attr.s(slots=True)
class Pre(ValueSegment):
    sep1 = attr.ib()
    tag = attr.ib()
    sep2 = attr.ib()


@attr.s(slots=True)
class Post(ValueSegment):
    sep1 = attr.ib()
    tag = attr.ib()
    sep2 = attr.ib()


@attr.s(slots=True)
class Dev(ValueSegment):
    sep = attr.ib()


@attr.s(slots=True)
class Local(ValueSegment):
    pass
