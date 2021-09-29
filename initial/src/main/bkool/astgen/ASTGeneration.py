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
        pass
    def visitClassDeclList(self, ctx: BKOOLParser.ClassDeclListContext):
        pass
    def visitClassDecl(self, ctx: BKOOLParser.ClassDeclContext):
        pass
    def visitMemberList(self, ctx: BKOOLParser.MemberListContext):
        pass
    def visitMember(self, ctx: BKOOLParser.MemberContext):
        pass
    def visitAttrKeyword(self, ctx: BKOOLParser.AttrKeywordContext):
        pass
    def visitAttrType(self, ctx: BKOOLParser.AttrTypeContext):
        pass
    def visitArrayType(self, ctx: BKOOLParser.ArrayTypeContext):
        pass
    def visitAttrList(self, ctx: BKOOLParser.AttrListContext):
        pass
    def visitAttribute(self, ctx: BKOOLParser.AttributeContext):
        pass
    def visitReturnType(self, ctx: BKOOLParser.ReturnTypeContext):
        pass
    def visitMethod(self, ctx: BKOOLParser.MethodContext):
        pass
    def visitParamList(self, ctx: BKOOLParser.ParamListContext):
        pass
    def visitParam(self, ctx: BKOOLParser.ParamContext):
        pass
    def visitIdList(self, ctx: BKOOLParser.IdListContext):
        pass

    def visitExp(self, ctx: BKOOLParser.ExpContext):
        pass
    def visitArgList(self, ctx: BKOOLParser.ArgListContext):
        pass
    def visitObj_create(self, ctx: BKOOLParser.Obj_createContext):
        pass

    def visitStmtList(self, ctx: BKOOLParser.StmtListContext):
        pass
    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        pass
    def visitBlockStmt(self, ctx: BKOOLParser.BlockStmtContext):
        pass
    def visitBlockBody(self, ctx: BKOOLParser.BlockBodyContext):
        pass
    def visitDeclList(self, ctx: BKOOLParser.DeclListContext):
        pass
    def visitDecl(self, ctx: BKOOLParser.DeclContext):
        pass
    def visitAssignStmt(self, ctx: BKOOLParser.AssignStmtContext):
        pass
    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        pass
    def visitIfStmt(self, ctx: BKOOLParser.IfStmtContext):
        pass
    def visitForStmt(self, ctx: BKOOLParser.ForStmtContext):
        pass
    def visitScalarVar(self, ctx: BKOOLParser.ScalarVarContext):
        pass
    def visitBreakStmt(self, ctx: BKOOLParser.BreakStmtContext):
        pass
    def visitContinueStmt(self, ctx: BKOOLParser.ContinueStmtContext):
        pass
    def visitReturnStmt(self, ctx: BKOOLParser.ReturnStmtContext):
        pass
    def visitMethodInvokeStmt(self, ctx: BKOOLParser.MethodInvokeStmtContext):
        pass