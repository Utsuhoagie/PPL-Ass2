from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):

    # def visit(self,ctx:BKOOLParser.Context):
    #     return ([self.visit(x) for x in ctx.classdecl()])

    # def visitClassdecl(self,ctx:BKOOLParser.ClassDeclContext):
    #     return ClassDecl(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.memdecl()])

    # def visitMemdecl(self,ctx):         #:BKOOLParser.MemDeclContext):
    #     return AttributeDecl(Instance(),VarDecl(Id(ctx.ID().getText()),self.visit(ctx.bkooltype())))

    # def visitBkooltype(self,ctx):       #:BKOOLParser.BkooltypeContext):
    #     return IntType() if ctx.INTTYPE() else VoidType()
        
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return
    def visitClassDeclList(self, ctx: BKOOLParser.ClassDeclListContext):
        return
    def visitClassDecl(self, ctx: BKOOLParser.ClassDeclContext):
        return
    def visitMemberList(self, ctx: BKOOLParser.MemberListContext):
        return
    def visitMember(self, ctx: BKOOLParser.MemberContext):
        return
    def visitAttrKeyword(self, ctx: BKOOLParser.AttrKeywordContext):
        return
    def visitAttrType(self, ctx: BKOOLParser.AttrTypeContext):
        return
    def visitArrayType(self, ctx: BKOOLParser.ArrayTypeContext):
        return
    def visitAttrList(self, ctx: BKOOLParser.AttrListContext):
        return
    def visitAttribute(self, ctx: BKOOLParser.AttributeContext):
        return
    def visitReturnType(self, ctx: BKOOLParser.ReturnTypeContext):
        return
    def visitMethod(self, ctx: BKOOLParser.MethodContext):
        return
    def visitParamList(self, ctx: BKOOLParser.ParamListContext):
        return
    def visitParam(self, ctx: BKOOLParser.ParamContext):
        return
    def visitIdList(self, ctx: BKOOLParser.IdListContext):
        return

    def visitExp(self, ctx: BKOOLParser.ExpContext):
        return
    def visitArgList(self, ctx: BKOOLParser.ArgListContext):
        return
    def visitObj_create(self, ctx: BKOOLParser.Obj_createContext):
        return

    def visitStmtList(self, ctx: BKOOLParser.StmtListContext):
        return
    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        return
    def visitBlockStmt(self, ctx: BKOOLParser.BlockStmtContext):
        return self.visit
    def visitBlockBody(self, ctx: BKOOLParser.BlockBodyContext):
        return
    def visitDeclList(self, ctx: BKOOLParser.DeclListContext):
        return
    def visitDecl(self, ctx: BKOOLParser.DeclContext):
        return
    def visitAssignStmt(self, ctx: BKOOLParser.AssignStmtContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.exp())
        return Assign(lhs, exp)

    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())   # 'local var'
        elif ctx.getChildCount() == 4:
            exp1 = self.visit(ctx.getChild(0))
            exp2 = self.visit(ctx.getChild(2))
            return ArrayCell(exp1, exp2)    # 'index op'
        else:
            exp = self.visit(ctx.exp())     # is None if 'static attr access'
            return FieldAccess(exp, ctx.ID().getText())     # 'attr access'

    def visitIfStmt(self, ctx: BKOOLParser.IfStmtContext) -> If:
        exp = self.visit(ctx.exp())
        stmtThen = self.visit(ctx.getChild(3))

        if ctx.getChildCount() > 4:
            stmtElse = self.visit(ctx.getChild(5))
            return If(exp, stmtThen, stmtElse)
        return If(exp, stmtThen)
        
    def visitForStmt(self, ctx: BKOOLParser.ForStmtContext):
        scalarVar = self.visit(ctx.scalarVar())
        expFrom = self.visit(ctx.getChild(3))
        expTo = self.visit(ctx.getChild(5))
        dir = True if ctx.TO() else False
        stmt = self.visit(ctx.stmt())
        return For(scalarVar, expFrom, expTo, dir, stmt)

    def visitScalarVar(self, ctx: BKOOLParser.ScalarVarContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())   # 'local var'
        elif ctx.getChildCount() == 4:
            exp1 = self.visit(ctx.getChild(0))
            exp2 = self.visit(ctx.getChild(2))
            return ArrayCell(exp1, exp2)    # 'index op'
        else:
            exp = self.visit(ctx.exp())     # is None if 'static attr access'
            return FieldAccess(exp, ctx.ID().getText())     # 'attr access'

    def visitBreakStmt(self, ctx: BKOOLParser.BreakStmtContext):
        return Break()
    def visitContinueStmt(self, ctx: BKOOLParser.ContinueStmtContext):
        return Continue()
    def visitReturnStmt(self, ctx: BKOOLParser.ReturnStmtContext):
        return Return(self.visit(ctx.exp()))
        
    def visitMethodInvokeStmt(self, ctx: BKOOLParser.MethodInvokeStmtContext):
        return