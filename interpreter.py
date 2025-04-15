import math
from gen.LangVisitor import LangVisitor

class Interpreter(LangVisitor):
    # Dict to store vars
    def __init__(self):
        self.variables = {}

    def visitPrintStmt(self, ctx):
        message = ctx.STRING().getText().strip('"')
        print(message)

    # Basic Math 
    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return left * right if op == '*' else left / right

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return left + right if op == '+' else left - right

    def visitIntExpr(self, ctx):
        return int(ctx.INT().getText())

    def visitParensExpr(self, ctx):
        return self.visit(ctx.expr())

    # Trigonometry
    def visitSinExpr(self, ctx):
        value = self.visit(ctx.expr())
        return math.sin(math.radians(value))

    def visitCosExpr(self, ctx):
        value = self.visit(ctx.expr())
        return math.cos(math.radians(value))

    def visitTanExpr(self, ctx):
        value = self.visit(ctx.expr())
        return math.tan(math.radians(value))

    # Vars
    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        return self.variables.get(name)

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[name] = value

    def visitExprStmt(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return value

    # Conditions & control 
    def visitCondition(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.comparisonOp().getText()

        if op == '==': return left == right
        if op == '!=': return left != right
        if op == '<':  return left < right
        if op == '<=': return left <= right
        if op == '>':  return left > right
        if op == '>=': return left >= right

    def visitIfStmt(self, ctx):
        if self.visit(ctx.condition()):
            for stmt in ctx.statement():
                self.visit(stmt)

    def visitForStmt(self, ctx):
        self.visit(ctx.assignment(0))
        while self.visit(ctx.condition()):
            for stmt in ctx.statement():
                self.visit(stmt)
            self.visit(ctx.assignment(1))

    def visitWhileStmt(self, ctx):
        while self.visit(ctx.condition()):
            for stmt in ctx.statement():
                self.visit(stmt)