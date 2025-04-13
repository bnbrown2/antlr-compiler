# Generated from Lang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete listener for a parse tree produced by LangParser.
class LangListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#program.
    def enterProgram(self, ctx:LangParser.ProgramContext):
        pass

    # Exit a parse tree produced by LangParser#program.
    def exitProgram(self, ctx:LangParser.ProgramContext):
        pass


    # Enter a parse tree produced by LangParser#statement.
    def enterStatement(self, ctx:LangParser.StatementContext):
        pass

    # Exit a parse tree produced by LangParser#statement.
    def exitStatement(self, ctx:LangParser.StatementContext):
        pass


    # Enter a parse tree produced by LangParser#printStmt.
    def enterPrintStmt(self, ctx:LangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by LangParser#printStmt.
    def exitPrintStmt(self, ctx:LangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by LangParser#exprStmt.
    def enterExprStmt(self, ctx:LangParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by LangParser#exprStmt.
    def exitExprStmt(self, ctx:LangParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by LangParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:LangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by LangParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:LangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by LangParser#ParensExpr.
    def enterParensExpr(self, ctx:LangParser.ParensExprContext):
        pass

    # Exit a parse tree produced by LangParser#ParensExpr.
    def exitParensExpr(self, ctx:LangParser.ParensExprContext):
        pass


    # Enter a parse tree produced by LangParser#IntExpr.
    def enterIntExpr(self, ctx:LangParser.IntExprContext):
        pass

    # Exit a parse tree produced by LangParser#IntExpr.
    def exitIntExpr(self, ctx:LangParser.IntExprContext):
        pass


    # Enter a parse tree produced by LangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:LangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by LangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:LangParser.AddSubExprContext):
        pass



del LangParser