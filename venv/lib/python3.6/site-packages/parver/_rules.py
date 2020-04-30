# coding: utf-8
from __future__ import absolute_import, division, print_function

from arpeggio import EOF, Optional
from arpeggio import RegExMatch as _
from arpeggio import ZeroOrMore


def alpha():
    return _(r'[0-9]*[a-z][a-z0-9]*')


def int_():
    return _(r'0|[1-9][0-9]*')


def dot():
    return '.'


def sep():
    return dot


def local_part():
    return [alpha, int_]


def local():
    return '+', local_part, ZeroOrMore(sep, local_part)


def dev():
    return sep, 'dev', int_


def post_tag():
    return 'post'


def pre_post_num():
    return int_


def post():
    return sep, post_tag, pre_post_num


def pre_tag():
    return ['a', 'b', 'rc']


def pre():
    return pre_tag, pre_post_num


def release():
    return int_, ZeroOrMore(dot, int_)


def epoch():
    return int_, '!'


def version():
    return (
        Optional(epoch),
        release,
        Optional(pre),
        Optional(post),
        Optional(dev),
        Optional(local),
        EOF,
    )
