# Generated from c2llvm.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .c2llvmParser import c2llvmParser
else:
    from c2llvmParser import c2llvmParser

# This class defines a complete generic visitor for a parse tree produced by c2llvmParser.

class c2llvmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by c2llvmParser#prog.
    def visitProg(self, ctx:c2llvmParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#include.
    def visitInclude(self, ctx:c2llvmParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#declaration.
    def visitDeclaration(self, ctx:c2llvmParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#structDeclaration.
    def visitStructDeclaration(self, ctx:c2llvmParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#structMemberDeclaration.
    def visitStructMemberDeclaration(self, ctx:c2llvmParser.StructMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#statement.
    def visitStatement(self, ctx:c2llvmParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#assignStatement.
    def visitAssignStatement(self, ctx:c2llvmParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#conditionStatement.
    def visitConditionStatement(self, ctx:c2llvmParser.ConditionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#ifStatement.
    def visitIfStatement(self, ctx:c2llvmParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#elseifStatement.
    def visitElseifStatement(self, ctx:c2llvmParser.ElseifStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#elseStatement.
    def visitElseStatement(self, ctx:c2llvmParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#whileStatement.
    def visitWhileStatement(self, ctx:c2llvmParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#forStatement.
    def visitForStatement(self, ctx:c2llvmParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#forInitStatement.
    def visitForInitStatement(self, ctx:c2llvmParser.ForInitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#forExecStatement.
    def visitForExecStatement(self, ctx:c2llvmParser.ForExecStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#returnStatement.
    def visitReturnStatement(self, ctx:c2llvmParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#breakStatement.
    def visitBreakStatement(self, ctx:c2llvmParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#continueStatement.
    def visitContinueStatement(self, ctx:c2llvmParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#variableDefinitionStatement.
    def visitVariableDefinitionStatement(self, ctx:c2llvmParser.VariableDefinitionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#arrayDefinitionStatement.
    def visitArrayDefinitionStatement(self, ctx:c2llvmParser.ArrayDefinitionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#structDefinitionStatement.
    def visitStructDefinitionStatement(self, ctx:c2llvmParser.StructDefinitionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vArrayItem.
    def visitVArrayItem(self, ctx:c2llvmParser.VArrayItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vStructMember.
    def visitVStructMember(self, ctx:c2llvmParser.VStructMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#funcStatement.
    def visitFuncStatement(self, ctx:c2llvmParser.FuncStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#funcExpression.
    def visitFuncExpression(self, ctx:c2llvmParser.FuncExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#paramsInvokePattern.
    def visitParamsInvokePattern(self, ctx:c2llvmParser.ParamsInvokePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#paramInvokePattern.
    def visitParamInvokePattern(self, ctx:c2llvmParser.ParamInvokePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:c2llvmParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#paramsDefinitionPattern.
    def visitParamsDefinitionPattern(self, ctx:c2llvmParser.ParamsDefinitionPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#paramDefinitionPattern.
    def visitParamDefinitionPattern(self, ctx:c2llvmParser.ParamDefinitionPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#FunctionExpr.
    def visitFunctionExpr(self, ctx:c2llvmParser.FunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#Or.
    def visitOr(self, ctx:c2llvmParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#AddSub.
    def visitAddSub(self, ctx:c2llvmParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#Parens.
    def visitParens(self, ctx:c2llvmParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#String.
    def visitString(self, ctx:c2llvmParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#Double.
    def visitDouble(self, ctx:c2llvmParser.DoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#Int.
    def visitInt(self, ctx:c2llvmParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#Neg.
    def visitNeg(self, ctx:c2llvmParser.NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#ArrayItem.
    def visitArrayItem(self, ctx:c2llvmParser.ArrayItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#MulDivMod.
    def visitMulDivMod(self, ctx:c2llvmParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#Char.
    def visitChar(self, ctx:c2llvmParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#And.
    def visitAnd(self, ctx:c2llvmParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#structMember.
    def visitStructMember(self, ctx:c2llvmParser.StructMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#Compare.
    def visitCompare(self, ctx:c2llvmParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#Id.
    def visitId(self, ctx:c2llvmParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vType.
    def visitVType(self, ctx:c2llvmParser.VTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vInt.
    def visitVInt(self, ctx:c2llvmParser.VIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vChar.
    def visitVChar(self, ctx:c2llvmParser.VCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vDouble.
    def visitVDouble(self, ctx:c2llvmParser.VDoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vString.
    def visitVString(self, ctx:c2llvmParser.VStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vId.
    def visitVId(self, ctx:c2llvmParser.VIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vStruct.
    def visitVStruct(self, ctx:c2llvmParser.VStructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vArray.
    def visitVArray(self, ctx:c2llvmParser.VArrayContext):
        return self.visitChildren(ctx)



del c2llvmParser