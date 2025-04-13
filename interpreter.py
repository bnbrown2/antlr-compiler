from gen.LangVisitor import LangVisitor

class Interpreter(LangVisitor):

    # Handle print statement
    def visitPrintStmt(self, ctx):
        text = ctx.STRING().getText()
        print(text.strip('"'))
        return None

    # arithmetic expression
    def visitExprStmt(self, ctx):
        result = self.visit(ctx.expr())
        print(result)  # Display arithmetic expression result
        return result


    # integer 
    def visitIntExpr(self, ctx):
        return int(ctx.INT().getText())

    # parentheses
    def visitParensExpr(self, ctx):
        return self.visit(ctx.expr())

    # multiplication and division 
    def visitMulDivExpr(self, ctx):
        leftSide = self.visit(ctx.expr(0))
        rightSide = self.visit(ctx.expr(1))

        if ctx.getChild(1).getText() == '*': # mult
            return leftSide * rightSide
        else:  # division
            if rightSide == 0:
                raise ValueError("Error: Division by zero")
            return leftSide / rightSide


    # addition and subtraction 
    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.getChild(1).getText() == '+': # addition
            return left + right
        else:  # subtraction
            return left - right