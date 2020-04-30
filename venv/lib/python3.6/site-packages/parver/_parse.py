# coding: utf-8
from __future__ import absolute_import, division, print_function

import attr
import six
from arpeggio import NoMatch, PTNodeVisitor, Terminal, visit_parse_tree
from arpeggio.cleanpeg import ParserPEG

from . import _segments as segment
from ._helpers import IMPLICIT_ZERO, UNSET

canonical = r'''
    version = epoch? release pre? post? dev? local? EOF
    epoch = int "!"
    release = int (dot int)*
    pre = pre_tag pre_post_num
    pre_tag = "a" / "b" / "rc"
    post = sep post_tag pre_post_num
    pre_post_num = int
    post_tag = "post"
    dev = sep "dev" int
    local = "+" local_part (sep local_part)*
    local_part = alpha / int
    sep = dot
    dot = "."
    int = r'0|[1-9][0-9]*'
    alpha = r'[0-9]*[a-z][a-z0-9]*'
'''

permissive = r'''
    version = v? epoch? release pre? (post / post_implicit)? dev? local? EOF
    v = "v"
    epoch = int "!"
    release = int (dot int)*
    pre = sep? pre_tag pre_post_num?
    pre_tag = "c" / "rc" / "alpha" / "a" / "beta" / "b" / "preview" / "pre"
    post = sep? post_tag pre_post_num?
    post_implicit = "-" int
    post_tag = "post" / "rev" / "r"
    pre_post_num = sep? int
    dev = sep? "dev" int?
    local = "+" local_part (sep local_part)*
    local_part = alpha / int
    sep = dot / "-" / "_"
    dot = "."
    int = r'[0-9]+'
    alpha = r'[0-9]*[a-z][a-z0-9]*'
'''

_strict_parser = ParserPEG(canonical, root_rule_name='version', skipws=False)
_permissive_parser = ParserPEG(
    permissive, root_rule_name='version', skipws=False, ignore_case=True)


@attr.s
class Token(object):
    value = attr.ib()


def make_token(name):
    return type(name, (Token,), dict())


Sep = make_token('Sep')
Tag = make_token('Tag')
VToken = make_token('VToken')


class VersionVisitor(PTNodeVisitor):
    def visit_version(self, node, children):
        return children

    def visit_v(self, node, children):
        return segment.V()

    def visit_epoch(self, node, children):
        return segment.Epoch(children[0])

    def visit_release(self, node, children):
        return segment.Release(tuple(children))

    def visit_pre(self, node, children):
        sep1 = UNSET
        tag = UNSET
        sep2 = UNSET
        num = UNSET

        for token in children:
            if sep1 is UNSET:
                if isinstance(token, Sep):
                    sep1 = token.value
                elif isinstance(token, Tag):
                    sep1 = None
                    tag = token.value
            elif tag is UNSET:
                tag = token.value
            else:
                assert isinstance(token, tuple)
                assert len(token) == 2
                sep2 = token[0].value
                num = token[1]

        if sep2 is UNSET:
            sep2 = None
            num = IMPLICIT_ZERO

        assert sep1 is not UNSET
        assert tag is not UNSET
        assert sep2 is not UNSET
        assert num is not UNSET

        return segment.Pre(sep1=sep1, tag=tag, sep2=sep2, value=num)

    def visit_pre_post_num(self, node, children):
        # when "pre_post_num = int", visit_int isn't called for some reason
        # I don't understand. Let's call int() manually
        if isinstance(node, Terminal):
            return Sep(None), int(node.value)

        if len(children) == 1:
            return Sep(None), children[0]
        else:
            return tuple(children[:2])

    def visit_pre_tag(self, node, children):
        return Tag(node.value)

    def visit_post(self, node, children):
        sep1 = UNSET
        tag = UNSET
        sep2 = UNSET
        num = UNSET

        for token in children:
            if sep1 is UNSET:
                if isinstance(token, Sep):
                    sep1 = token.value
                elif isinstance(token, Tag):
                    sep1 = None
                    tag = token.value
            elif tag is UNSET:
                tag = token.value
            else:
                assert isinstance(token, tuple)
                assert len(token) == 2
                sep2 = token[0].value
                num = token[1]

        if sep2 is UNSET:
            sep2 = None
            num = IMPLICIT_ZERO

        assert sep1 is not UNSET
        assert tag is not UNSET
        assert sep2 is not UNSET
        assert num is not UNSET

        return segment.Post(sep1=sep1, tag=tag, sep2=sep2, value=num)

    def visit_post_tag(self, node, children):
        return Tag(node.value)

    def visit_post_implicit(self, node, children):
        return segment.Post(sep1=UNSET, tag=None, sep2=UNSET, value=children[0])

    def visit_dev(self, node, children):
        num = IMPLICIT_ZERO
        sep = UNSET

        for token in children:
            if sep is UNSET:
                if isinstance(token, Sep):
                    sep = token.value
                else:
                    num = token
            else:
                num = token

        if sep is UNSET:
            sep = None

        return segment.Dev(value=num, sep=sep)

    def visit_local(self, node, children):
        return segment.Local(''.join(str(getattr(c, 'value', c)) for c in children))

    def visit_int(self, node, children):
        return int(node.value)

    def visit_sep(self, node, children):
        return Sep(node.value)


class ParseError(ValueError):
    """Raised when parsing an invalid version number."""


def parse(version, strict=False):
    parser = _strict_parser if strict else _permissive_parser

    try:
        tree = parser.parse(version.strip())
    except NoMatch as exc:
        six.raise_from(ParseError(str(exc)), None)

    return visit_parse_tree(tree, VersionVisitor())
