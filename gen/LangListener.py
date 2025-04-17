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


    # Enter a parse tree produced by LangParser#IdExpr.
    def enterIdExpr(self, ctx:LangParser.IdExprContext):
        pass

    # Exit a parse tree produced by LangParser#IdExpr.
    def exitIdExpr(self, ctx:LangParser.IdExprContext):
        pass


    # Enter a parse tree produced by LangParser#TanExpr.
    def enterTanExpr(self, ctx:LangParser.TanExprContext):
        pass

    # Exit a parse tree produced by LangParser#TanExpr.
    def exitTanExpr(self, ctx:LangParser.TanExprContext):
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


    # Enter a parse tree produced by LangParser#SinExpr.
    def enterSinExpr(self, ctx:LangParser.SinExprContext):
        pass

    # Exit a parse tree produced by LangParser#SinExpr.
    def exitSinExpr(self, ctx:LangParser.SinExprContext):
        pass


    # Enter a parse tree produced by LangParser#CosExpr.
    def enterCosExpr(self, ctx:LangParser.CosExprContext):
        pass

    # Exit a parse tree produced by LangParser#CosExpr.
    def exitCosExpr(self, ctx:LangParser.CosExprContext):
        pass


    # Enter a parse tree produced by LangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:LangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by LangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:LangParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by LangParser#assignment.
    def enterAssignment(self, ctx:LangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LangParser#assignment.
    def exitAssignment(self, ctx:LangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LangParser#ifStmt.
    def enterIfStmt(self, ctx:LangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by LangParser#ifStmt.
    def exitIfStmt(self, ctx:LangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by LangParser#forStmt.
    def enterForStmt(self, ctx:LangParser.ForStmtContext):
        pass

    # Exit a parse tree produced by LangParser#forStmt.
    def exitForStmt(self, ctx:LangParser.ForStmtContext):
        pass


    # Enter a parse tree produced by LangParser#whileStmt.
    def enterWhileStmt(self, ctx:LangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by LangParser#whileStmt.
    def exitWhileStmt(self, ctx:LangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by LangParser#condition.
    def enterCondition(self, ctx:LangParser.ConditionContext):
        pass

    # Exit a parse tree produced by LangParser#condition.
    def exitCondition(self, ctx:LangParser.ConditionContext):
        pass


    # Enter a parse tree produced by LangParser#comparisonOp.
    def enterComparisonOp(self, ctx:LangParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by LangParser#comparisonOp.
    def exitComparisonOp(self, ctx:LangParser.ComparisonOpContext):
        pass



del LangParser