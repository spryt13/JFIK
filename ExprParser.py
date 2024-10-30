# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,159,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,1,1,1,3,1,36,8,1,1,1,1,1,5,1,40,8,1,10,1,
        12,1,43,9,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,5,5,54,8,5,10,5,
        12,5,57,9,5,1,6,1,6,1,6,1,6,1,6,3,6,64,8,6,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,8,1,8,1,8,5,8,76,8,8,10,8,12,8,79,9,8,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,3,10,101,8,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,
        109,8,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,
        121,8,12,10,12,12,12,124,9,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,
        132,8,13,10,13,12,13,135,9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,151,8,14,10,14,12,14,154,
        9,14,1,14,3,14,157,8,14,1,14,0,2,24,26,15,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,0,0,162,0,30,1,0,0,0,2,41,1,0,0,0,4,44,1,0,0,0,
        6,46,1,0,0,0,8,48,1,0,0,0,10,55,1,0,0,0,12,58,1,0,0,0,14,70,1,0,
        0,0,16,72,1,0,0,0,18,80,1,0,0,0,20,108,1,0,0,0,22,110,1,0,0,0,24,
        114,1,0,0,0,26,125,1,0,0,0,28,156,1,0,0,0,30,31,3,2,1,0,31,32,5,
        0,0,1,32,1,1,0,0,0,33,36,3,20,10,0,34,36,3,12,6,0,35,33,1,0,0,0,
        35,34,1,0,0,0,36,37,1,0,0,0,37,38,5,7,0,0,38,40,1,0,0,0,39,35,1,
        0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,
        41,1,0,0,0,44,45,3,2,1,0,45,5,1,0,0,0,46,47,3,2,1,0,47,7,1,0,0,0,
        48,49,3,2,1,0,49,9,1,0,0,0,50,51,3,20,10,0,51,52,5,7,0,0,52,54,1,
        0,0,0,53,50,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,
        11,1,0,0,0,57,55,1,0,0,0,58,59,5,16,0,0,59,60,5,15,0,0,60,61,3,14,
        7,0,61,63,5,1,0,0,62,64,3,16,8,0,63,62,1,0,0,0,63,64,1,0,0,0,64,
        65,1,0,0,0,65,66,5,2,0,0,66,67,5,3,0,0,67,68,3,10,5,0,68,69,5,4,
        0,0,69,13,1,0,0,0,70,71,5,22,0,0,71,15,1,0,0,0,72,77,3,18,9,0,73,
        74,5,5,0,0,74,76,3,18,9,0,75,73,1,0,0,0,76,79,1,0,0,0,77,75,1,0,
        0,0,77,78,1,0,0,0,78,17,1,0,0,0,79,77,1,0,0,0,80,81,3,28,14,0,81,
        19,1,0,0,0,82,83,5,11,0,0,83,109,3,24,12,0,84,85,5,22,0,0,85,86,
        5,6,0,0,86,109,3,24,12,0,87,88,5,12,0,0,88,89,5,15,0,0,89,109,5,
        22,0,0,90,91,5,17,0,0,91,92,3,22,11,0,92,93,5,3,0,0,93,94,3,4,2,
        0,94,100,5,4,0,0,95,96,5,18,0,0,96,97,5,3,0,0,97,98,3,6,3,0,98,99,
        5,4,0,0,99,101,1,0,0,0,100,95,1,0,0,0,100,101,1,0,0,0,101,109,1,
        0,0,0,102,103,5,19,0,0,103,104,3,22,11,0,104,105,5,3,0,0,105,106,
        3,8,4,0,106,107,5,4,0,0,107,109,1,0,0,0,108,82,1,0,0,0,108,84,1,
        0,0,0,108,87,1,0,0,0,108,90,1,0,0,0,108,102,1,0,0,0,109,21,1,0,0,
        0,110,111,3,28,14,0,111,112,5,10,0,0,112,113,3,28,14,0,113,23,1,
        0,0,0,114,115,6,12,-1,0,115,116,3,26,13,0,116,122,1,0,0,0,117,118,
        10,1,0,0,118,119,5,8,0,0,119,121,3,24,12,2,120,117,1,0,0,0,121,124,
        1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,25,1,0,0,0,124,122,1,
        0,0,0,125,126,6,13,-1,0,126,127,3,28,14,0,127,133,1,0,0,0,128,129,
        10,1,0,0,129,130,5,9,0,0,130,132,3,26,13,2,131,128,1,0,0,0,132,135,
        1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,27,1,0,0,0,135,133,1,
        0,0,0,136,157,5,22,0,0,137,157,5,20,0,0,138,157,5,21,0,0,139,140,
        5,13,0,0,140,157,3,28,14,0,141,142,5,14,0,0,142,157,3,28,14,0,143,
        144,5,1,0,0,144,145,3,24,12,0,145,146,5,2,0,0,146,157,1,0,0,0,147,
        148,5,22,0,0,148,152,5,1,0,0,149,151,3,28,14,0,150,149,1,0,0,0,151,
        154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,155,1,0,0,0,154,
        152,1,0,0,0,155,157,5,2,0,0,156,136,1,0,0,0,156,137,1,0,0,0,156,
        138,1,0,0,0,156,139,1,0,0,0,156,141,1,0,0,0,156,143,1,0,0,0,156,
        147,1,0,0,0,157,29,1,0,0,0,11,35,41,55,63,77,100,108,122,133,152,
        156
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "','", "'='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'print'", "'read'", "'toint'", "'toreal'", "<INVALID>", 
                     "'function'", "'if'", "'else'", "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NEWLINE", 
                      "ADDSUBSIGN", "MULDIVSIGN", "COND_OP", "PRINT", "READ", 
                      "TOINT", "TOREAL", "TYPE", "FUNCTION", "IF", "ELSE", 
                      "WHILE", "INT", "REAL", "ID", "WS" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_blockif = 2
    RULE_blockelse = 3
    RULE_blockwhile = 4
    RULE_blockfunc = 5
    RULE_func = 6
    RULE_namefunc = 7
    RULE_paramsfunc = 8
    RULE_paramfunc = 9
    RULE_stat = 10
    RULE_cond = 11
    RULE_expr = 12
    RULE_expr_follow = 13
    RULE_value = 14

    ruleNames =  [ "prog", "block", "blockif", "blockelse", "blockwhile", 
                   "blockfunc", "func", "namefunc", "paramsfunc", "paramfunc", 
                   "stat", "cond", "expr", "expr_follow", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NEWLINE=7
    ADDSUBSIGN=8
    MULDIVSIGN=9
    COND_OP=10
    PRINT=11
    READ=12
    TOINT=13
    TOREAL=14
    TYPE=15
    FUNCTION=16
    IF=17
    ELSE=18
    WHILE=19
    INT=20
    REAL=21
    ID=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.block()
            self.state = 31
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.FuncContext)
            else:
                return self.getTypedRuleContext(ExprParser.FuncContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ExprParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4921344) != 0):
                self.state = 35
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 12, 17, 19, 22]:
                    self.state = 33
                    self.stat()
                    pass
                elif token in [16]:
                    self.state = 34
                    self.func()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 37
                self.match(ExprParser.NEWLINE)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_blockif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockif" ):
                listener.enterBlockif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockif" ):
                listener.exitBlockif(self)




    def blockif(self):

        localctx = ExprParser.BlockifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_blockif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_blockelse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockelse" ):
                listener.enterBlockelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockelse" ):
                listener.exitBlockelse(self)




    def blockelse(self):

        localctx = ExprParser.BlockelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_blockelse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_blockwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockwhile" ):
                listener.enterBlockwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockwhile" ):
                listener.exitBlockwhile(self)




    def blockwhile(self):

        localctx = ExprParser.BlockwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_blockwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def getRuleIndex(self):
            return ExprParser.RULE_blockfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockfunc" ):
                listener.enterBlockfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockfunc" ):
                listener.exitBlockfunc(self)




    def blockfunc(self):

        localctx = ExprParser.BlockfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_blockfunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4855808) != 0):
                self.state = 50
                self.stat()
                self.state = 51
                self.match(ExprParser.NEWLINE)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(ExprParser.FUNCTION, 0)

        def TYPE(self):
            return self.getToken(ExprParser.TYPE, 0)

        def namefunc(self):
            return self.getTypedRuleContext(ExprParser.NamefuncContext,0)


        def blockfunc(self):
            return self.getTypedRuleContext(ExprParser.BlockfuncContext,0)


        def paramsfunc(self):
            return self.getTypedRuleContext(ExprParser.ParamsfuncContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = ExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ExprParser.FUNCTION)
            self.state = 59
            self.match(ExprParser.TYPE)
            self.state = 60
            self.namefunc()
            self.state = 61
            self.match(ExprParser.T__0)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7364610) != 0):
                self.state = 62
                self.paramsfunc()


            self.state = 65
            self.match(ExprParser.T__1)
            self.state = 66
            self.match(ExprParser.T__2)
            self.state = 67
            self.blockfunc()
            self.state = 68
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamefuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_namefunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamefunc" ):
                listener.enterNamefunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamefunc" ):
                listener.exitNamefunc(self)




    def namefunc(self):

        localctx = ExprParser.NamefuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_namefunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramfunc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ParamfuncContext)
            else:
                return self.getTypedRuleContext(ExprParser.ParamfuncContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_paramsfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamsfunc" ):
                listener.enterParamsfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamsfunc" ):
                listener.exitParamsfunc(self)




    def paramsfunc(self):

        localctx = ExprParser.ParamsfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramsfunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.paramfunc()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 73
                self.match(ExprParser.T__4)
                self.state = 74
                self.paramfunc()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(ExprParser.ValueContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_paramfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamfunc" ):
                listener.enterParamfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamfunc" ):
                listener.exitParamfunc(self)




    def paramfunc(self):

        localctx = ExprParser.ParamfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)


    class ReadContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(ExprParser.READ, 0)
        def TYPE(self):
            return self.getToken(ExprParser.TYPE, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)


    class WhileContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)
        def cond(self):
            return self.getTypedRuleContext(ExprParser.CondContext,0)

        def blockwhile(self):
            return self.getTypedRuleContext(ExprParser.BlockwhileContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)


    class IfContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)
        def cond(self):
            return self.getTypedRuleContext(ExprParser.CondContext,0)

        def blockif(self):
            return self.getTypedRuleContext(ExprParser.BlockifContext,0)

        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)
        def blockelse(self):
            return self.getTypedRuleContext(ExprParser.BlockelseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = ExprParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(ExprParser.PRINT)
                self.state = 83
                self.expr(0)
                pass
            elif token in [22]:
                localctx = ExprParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(ExprParser.ID)
                self.state = 85
                self.match(ExprParser.T__5)
                self.state = 86
                self.expr(0)
                pass
            elif token in [12]:
                localctx = ExprParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.match(ExprParser.READ)
                self.state = 88
                self.match(ExprParser.TYPE)
                self.state = 89
                self.match(ExprParser.ID)
                pass
            elif token in [17]:
                localctx = ExprParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.match(ExprParser.IF)
                self.state = 91
                self.cond()
                self.state = 92
                self.match(ExprParser.T__2)
                self.state = 93
                self.blockif()
                self.state = 94
                self.match(ExprParser.T__3)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 95
                    self.match(ExprParser.ELSE)
                    self.state = 96
                    self.match(ExprParser.T__2)
                    self.state = 97
                    self.blockelse()
                    self.state = 98
                    self.match(ExprParser.T__3)


                pass
            elif token in [19]:
                localctx = ExprParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.match(ExprParser.WHILE)
                self.state = 103
                self.cond()
                self.state = 104
                self.match(ExprParser.T__2)
                self.state = 105
                self.blockwhile()
                self.state = 106
                self.match(ExprParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ValueContext)
            else:
                return self.getTypedRuleContext(ExprParser.ValueContext,i)


        def COND_OP(self):
            return self.getToken(ExprParser.COND_OP, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = ExprParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.value()
            self.state = 111
            self.match(ExprParser.COND_OP)
            self.state = 112
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class To_expr_followContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_follow(self):
            return self.getTypedRuleContext(ExprParser.Expr_followContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTo_expr_follow" ):
                listener.enterTo_expr_follow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTo_expr_follow" ):
                listener.exitTo_expr_follow(self)


    class AddsubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def ADDSUBSIGN(self):
            return self.getToken(ExprParser.ADDSUBSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddsub" ):
                listener.enterAddsub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddsub" ):
                listener.exitAddsub(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.To_expr_followContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 115
            self.expr_follow(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.AddsubContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 117
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 118
                    self.match(ExprParser.ADDSUBSIGN)
                    self.state = 119
                    self.expr(2) 
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_followContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr_follow

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class To_valueContext(Expr_followContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.Expr_followContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(ExprParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTo_value" ):
                listener.enterTo_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTo_value" ):
                listener.exitTo_value(self)


    class MuldivContext(Expr_followContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.Expr_followContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_follow(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Expr_followContext)
            else:
                return self.getTypedRuleContext(ExprParser.Expr_followContext,i)

        def MULDIVSIGN(self):
            return self.getToken(ExprParser.MULDIVSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMuldiv" ):
                listener.enterMuldiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMuldiv" ):
                listener.exitMuldiv(self)



    def expr_follow(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.Expr_followContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr_follow, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.To_valueContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 126
            self.value()
            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.MuldivContext(self, ExprParser.Expr_followContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_follow)
                    self.state = 128
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 129
                    self.match(ExprParser.MULDIVSIGN)
                    self.state = 130
                    self.expr_follow(2) 
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)


    class TointContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOINT(self):
            return self.getToken(ExprParser.TOINT, 0)
        def value(self):
            return self.getTypedRuleContext(ExprParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToint" ):
                listener.enterToint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToint" ):
                listener.exitToint(self)


    class TorealContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOREAL(self):
            return self.getToken(ExprParser.TOREAL, 0)
        def value(self):
            return self.getTypedRuleContext(ExprParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToreal" ):
                listener.enterToreal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToreal" ):
                listener.exitToreal(self)


    class IdContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class RealContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REAL(self):
            return self.getToken(ExprParser.REAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReal" ):
                listener.enterReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReal" ):
                listener.exitReal(self)


    class CallfuncContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ValueContext)
            else:
                return self.getTypedRuleContext(ExprParser.ValueContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallfunc" ):
                listener.enterCallfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallfunc" ):
                listener.exitCallfunc(self)


    class IntContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def value(self):

        localctx = ExprParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = ExprParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                localctx = ExprParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(ExprParser.INT)
                pass

            elif la_ == 3:
                localctx = ExprParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.match(ExprParser.REAL)
                pass

            elif la_ == 4:
                localctx = ExprParser.TointContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.match(ExprParser.TOINT)
                self.state = 140
                self.value()
                pass

            elif la_ == 5:
                localctx = ExprParser.TorealContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.match(ExprParser.TOREAL)
                self.state = 142
                self.value()
                pass

            elif la_ == 6:
                localctx = ExprParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 143
                self.match(ExprParser.T__0)
                self.state = 144
                self.expr(0)
                self.state = 145
                self.match(ExprParser.T__1)
                pass

            elif la_ == 7:
                localctx = ExprParser.CallfuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 147
                self.match(ExprParser.ID)
                self.state = 148
                self.match(ExprParser.T__0)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7364610) != 0):
                    self.state = 149
                    self.value()
                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 155
                self.match(ExprParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_sempred
        self._predicates[13] = self.expr_follow_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expr_follow_sempred(self, localctx:Expr_followContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




