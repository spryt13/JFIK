# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass


    # Enter a parse tree produced by ExprParser#blockif.
    def enterBlockif(self, ctx:ExprParser.BlockifContext):
        pass

    # Exit a parse tree produced by ExprParser#blockif.
    def exitBlockif(self, ctx:ExprParser.BlockifContext):
        pass


    # Enter a parse tree produced by ExprParser#blockelse.
    def enterBlockelse(self, ctx:ExprParser.BlockelseContext):
        pass

    # Exit a parse tree produced by ExprParser#blockelse.
    def exitBlockelse(self, ctx:ExprParser.BlockelseContext):
        pass


    # Enter a parse tree produced by ExprParser#blockwhile.
    def enterBlockwhile(self, ctx:ExprParser.BlockwhileContext):
        pass

    # Exit a parse tree produced by ExprParser#blockwhile.
    def exitBlockwhile(self, ctx:ExprParser.BlockwhileContext):
        pass


    # Enter a parse tree produced by ExprParser#blockfunc.
    def enterBlockfunc(self, ctx:ExprParser.BlockfuncContext):
        pass

    # Exit a parse tree produced by ExprParser#blockfunc.
    def exitBlockfunc(self, ctx:ExprParser.BlockfuncContext):
        pass


    # Enter a parse tree produced by ExprParser#func.
    def enterFunc(self, ctx:ExprParser.FuncContext):
        pass

    # Exit a parse tree produced by ExprParser#func.
    def exitFunc(self, ctx:ExprParser.FuncContext):
        pass


    # Enter a parse tree produced by ExprParser#namefunc.
    def enterNamefunc(self, ctx:ExprParser.NamefuncContext):
        pass

    # Exit a parse tree produced by ExprParser#namefunc.
    def exitNamefunc(self, ctx:ExprParser.NamefuncContext):
        pass


    # Enter a parse tree produced by ExprParser#paramsfunc.
    def enterParamsfunc(self, ctx:ExprParser.ParamsfuncContext):
        pass

    # Exit a parse tree produced by ExprParser#paramsfunc.
    def exitParamsfunc(self, ctx:ExprParser.ParamsfuncContext):
        pass


    # Enter a parse tree produced by ExprParser#paramfunc.
    def enterParamfunc(self, ctx:ExprParser.ParamfuncContext):
        pass

    # Exit a parse tree produced by ExprParser#paramfunc.
    def exitParamfunc(self, ctx:ExprParser.ParamfuncContext):
        pass


    # Enter a parse tree produced by ExprParser#print.
    def enterPrint(self, ctx:ExprParser.PrintContext):
        pass

    # Exit a parse tree produced by ExprParser#print.
    def exitPrint(self, ctx:ExprParser.PrintContext):
        pass


    # Enter a parse tree produced by ExprParser#assign.
    def enterAssign(self, ctx:ExprParser.AssignContext):
        pass

    # Exit a parse tree produced by ExprParser#assign.
    def exitAssign(self, ctx:ExprParser.AssignContext):
        pass


    # Enter a parse tree produced by ExprParser#read.
    def enterRead(self, ctx:ExprParser.ReadContext):
        pass

    # Exit a parse tree produced by ExprParser#read.
    def exitRead(self, ctx:ExprParser.ReadContext):
        pass


    # Enter a parse tree produced by ExprParser#if.
    def enterIf(self, ctx:ExprParser.IfContext):
        pass

    # Exit a parse tree produced by ExprParser#if.
    def exitIf(self, ctx:ExprParser.IfContext):
        pass


    # Enter a parse tree produced by ExprParser#while.
    def enterWhile(self, ctx:ExprParser.WhileContext):
        pass

    # Exit a parse tree produced by ExprParser#while.
    def exitWhile(self, ctx:ExprParser.WhileContext):
        pass


    # Enter a parse tree produced by ExprParser#cond.
    def enterCond(self, ctx:ExprParser.CondContext):
        pass

    # Exit a parse tree produced by ExprParser#cond.
    def exitCond(self, ctx:ExprParser.CondContext):
        pass


    # Enter a parse tree produced by ExprParser#to_expr_follow.
    def enterTo_expr_follow(self, ctx:ExprParser.To_expr_followContext):
        pass

    # Exit a parse tree produced by ExprParser#to_expr_follow.
    def exitTo_expr_follow(self, ctx:ExprParser.To_expr_followContext):
        pass


    # Enter a parse tree produced by ExprParser#addsub.
    def enterAddsub(self, ctx:ExprParser.AddsubContext):
        pass

    # Exit a parse tree produced by ExprParser#addsub.
    def exitAddsub(self, ctx:ExprParser.AddsubContext):
        pass


    # Enter a parse tree produced by ExprParser#to_value.
    def enterTo_value(self, ctx:ExprParser.To_valueContext):
        pass

    # Exit a parse tree produced by ExprParser#to_value.
    def exitTo_value(self, ctx:ExprParser.To_valueContext):
        pass


    # Enter a parse tree produced by ExprParser#muldiv.
    def enterMuldiv(self, ctx:ExprParser.MuldivContext):
        pass

    # Exit a parse tree produced by ExprParser#muldiv.
    def exitMuldiv(self, ctx:ExprParser.MuldivContext):
        pass


    # Enter a parse tree produced by ExprParser#id.
    def enterId(self, ctx:ExprParser.IdContext):
        pass

    # Exit a parse tree produced by ExprParser#id.
    def exitId(self, ctx:ExprParser.IdContext):
        pass


    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx:ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx:ExprParser.IntContext):
        pass


    # Enter a parse tree produced by ExprParser#real.
    def enterReal(self, ctx:ExprParser.RealContext):
        pass

    # Exit a parse tree produced by ExprParser#real.
    def exitReal(self, ctx:ExprParser.RealContext):
        pass


    # Enter a parse tree produced by ExprParser#toint.
    def enterToint(self, ctx:ExprParser.TointContext):
        pass

    # Exit a parse tree produced by ExprParser#toint.
    def exitToint(self, ctx:ExprParser.TointContext):
        pass


    # Enter a parse tree produced by ExprParser#toreal.
    def enterToreal(self, ctx:ExprParser.TorealContext):
        pass

    # Exit a parse tree produced by ExprParser#toreal.
    def exitToreal(self, ctx:ExprParser.TorealContext):
        pass


    # Enter a parse tree produced by ExprParser#par.
    def enterPar(self, ctx:ExprParser.ParContext):
        pass

    # Exit a parse tree produced by ExprParser#par.
    def exitPar(self, ctx:ExprParser.ParContext):
        pass


    # Enter a parse tree produced by ExprParser#callfunc.
    def enterCallfunc(self, ctx:ExprParser.CallfuncContext):
        pass

    # Exit a parse tree produced by ExprParser#callfunc.
    def exitCallfunc(self, ctx:ExprParser.CallfuncContext):
        pass



del ExprParser