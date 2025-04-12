from gen.LangVisitor import LangVisitor

class Interpreter(LangVisitor):
    def visitPrintStmt(self, ctx):
        text = ctx.STRING().getText()
        print(text.strip('"'))
        return None