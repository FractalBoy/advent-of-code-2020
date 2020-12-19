#!/usr/bin/env python

import sys

from sly import Lexer, Parser

from aoc_input import read_input


class CalcLexer(Lexer):
    tokens = {NUMBER}
    ignore = " \t"
    literals = {"+", "*", "(", ")"}

    @_(r"\d+")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    def error(self, t):
        print(f"Illegal character '{t.value[0]}'", file=sys.stderr)
        self.index += 1


class BasicCalcParser(Parser):
    tokens = CalcLexer.tokens
    precedence = (("left", "+", "*"),)

    @_("expr")
    def statement(self, p):
        return p.expr

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER


class AdvancedCalcParser(Parser):
    tokens = CalcLexer.tokens
    precedence = (
        ("left", "*"),
        ("left", "+"),
    )

    @_("expr")
    def statement(self, p):
        return p.expr

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER
