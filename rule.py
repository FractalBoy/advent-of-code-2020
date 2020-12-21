import sys
from itertools import chain

from sly import Lexer, Parser


class RuleLexer(Lexer):
    tokens = {NUMBER, LETTER, SPACE}
    literals = {"|", ":"}

    SPACE = r" "

    @_(r'"[a-z]"')
    def LETTER(self, t):
        t.value = t.value[1]
        return t

    @_(r"\d+")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    def error(self, t):
        print(f"Illegal character '{t.value[0]}'", file=sys.stderr)
        self.index += 1


class RuleParser(Parser):
    tokens = RuleLexer.tokens
    precedence = (("left", "|"), ("left", SPACE))

    @_('rule')
    def statement(self, p):
        return p.rule

    @_("number_rule")
    def rule(self, p):
        return p.number_rule

    @_("LETTER")
    def rule(self, p):
        return p.LETTER

    @_('number_rule "|" number_rule')
    def number_rule(self, p):
        return (p.number_rule0, "or", p.number_rule1)

    @_("number_rule SPACE number_rule")
    def number_rule(self, p):
        return (p.number_rule0, "then", p.number_rule1)

    @_("NUMBER")
    def number_rule(self, p):
        return p.NUMBER
