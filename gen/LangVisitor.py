# Generated from Lang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete generic visitor for a parse tree produced by LangParser.

class LangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LangParser#program.
    def visitProgram(self, ctx:LangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#statement.
    def visitStatement(self, ctx:LangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#printStmt.
    def visitPrintStmt(self, ctx:LangParser.PrintStmtContext):
        return self.visitChildren(ctx)



del LangParser