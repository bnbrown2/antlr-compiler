# Generated from Lang.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,41,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,5,4,28,8,4,
        10,4,12,4,31,9,4,1,4,1,4,1,5,4,5,36,8,5,11,5,12,5,37,1,5,1,5,1,29,
        0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,1,3,0,9,10,13,13,32,32,42,0,1,1,
        0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,
        0,1,13,1,0,0,0,3,15,1,0,0,0,5,21,1,0,0,0,7,23,1,0,0,0,9,25,1,0,0,
        0,11,35,1,0,0,0,13,14,5,59,0,0,14,2,1,0,0,0,15,16,5,112,0,0,16,17,
        5,114,0,0,17,18,5,105,0,0,18,19,5,110,0,0,19,20,5,116,0,0,20,4,1,
        0,0,0,21,22,5,40,0,0,22,6,1,0,0,0,23,24,5,41,0,0,24,8,1,0,0,0,25,
        29,5,34,0,0,26,28,9,0,0,0,27,26,1,0,0,0,28,31,1,0,0,0,29,30,1,0,
        0,0,29,27,1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,34,0,0,33,
        10,1,0,0,0,34,36,7,0,0,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,
        0,37,38,1,0,0,0,38,39,1,0,0,0,39,40,6,5,0,0,40,12,1,0,0,0,3,0,29,
        37,1,6,0,0
    ]

class LangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    STRING = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'print'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "STRING", "WS" ]

    grammarFileName = "Lang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


