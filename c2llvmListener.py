# Generated from c2llvm.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .c2llvmParser import c2llvmParser
else:
    from c2llvmParser import c2llvmParser

# This class defines a complete listener for a parse tree produced by c2llvmParser.
class c2llvmListener(ParseTreeListener):

    # Enter a parse tree produced by c2llvmParser#prog.
    def enterProg(self, ctx:c2llvmParser.ProgContext):
        pass

    # Exit a parse tree produced by c2llvmParser#prog.
    def exitProg(self, ctx:c2llvmParser.ProgContext):
        pass


    # Enter a parse tree produced by c2llvmParser#include.
    def enterInclude(self, ctx:c2llvmParser.IncludeContext):
        pass

    # Exit a parse tree produced by c2llvmParser#include.
    def exitInclude(self, ctx:c2llvmParser.IncludeContext):
        pass


    # Enter a parse tree produced by c2llvmParser#declaration.
    def enterDeclaration(self, ctx:c2llvmParser.DeclarationContext):
        pass

    # Exit a parse tree produced by c2llvmParser#declaration.
    def exitDeclaration(self, ctx:c2llvmParser.DeclarationContext):
        pass


    # Enter a parse tree produced by c2llvmParser#statement.
    def enterStatement(self, ctx:c2llvmParser.StatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#statement.
    def exitStatement(self, ctx:c2llvmParser.StatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#assignStatement.
    def enterAssignStatement(self, ctx:c2llvmParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#assignStatement.
    def exitAssignStatement(self, ctx:c2llvmParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#ifStatement.
    def enterIfStatement(self, ctx:c2llvmParser.IfStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#ifStatement.
    def exitIfStatement(self, ctx:c2llvmParser.IfStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#elseifStatement.
    def enterElseifStatement(self, ctx:c2llvmParser.ElseifStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#elseifStatement.
    def exitElseifStatement(self, ctx:c2llvmParser.ElseifStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#elseStatement.
    def enterElseStatement(self, ctx:c2llvmParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#elseStatement.
    def exitElseStatement(self, ctx:c2llvmParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#whileStatement.
    def enterWhileStatement(self, ctx:c2llvmParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#whileStatement.
    def exitWhileStatement(self, ctx:c2llvmParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#forStatement.
    def enterForStatement(self, ctx:c2llvmParser.ForStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#forStatement.
    def exitForStatement(self, ctx:c2llvmParser.ForStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#forInitStatement.
    def enterForInitStatement(self, ctx:c2llvmParser.ForInitStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#forInitStatement.
    def exitForInitStatement(self, ctx:c2llvmParser.ForInitStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#forExecStatement.
    def enterForExecStatement(self, ctx:c2llvmParser.ForExecStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#forExecStatement.
    def exitForExecStatement(self, ctx:c2llvmParser.ForExecStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#returnStatement.
    def enterReturnStatement(self, ctx:c2llvmParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#returnStatement.
    def exitReturnStatement(self, ctx:c2llvmParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#breakStatement.
    def enterBreakStatement(self, ctx:c2llvmParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#breakStatement.
    def exitBreakStatement(self, ctx:c2llvmParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#continueStatement.
    def enterContinueStatement(self, ctx:c2llvmParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#continueStatement.
    def exitContinueStatement(self, ctx:c2llvmParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#variableDefinitionStatement.
    def enterVariableDefinitionStatement(self, ctx:c2llvmParser.VariableDefinitionStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#variableDefinitionStatement.
    def exitVariableDefinitionStatement(self, ctx:c2llvmParser.VariableDefinitionStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#funcStatement.
    def enterFuncStatement(self, ctx:c2llvmParser.FuncStatementContext):
        pass

    # Exit a parse tree produced by c2llvmParser#funcStatement.
    def exitFuncStatement(self, ctx:c2llvmParser.FuncStatementContext):
        pass


    # Enter a parse tree produced by c2llvmParser#paramsInvokePattern.
    def enterParamsInvokePattern(self, ctx:c2llvmParser.ParamsInvokePatternContext):
        pass

    # Exit a parse tree produced by c2llvmParser#paramsInvokePattern.
    def exitParamsInvokePattern(self, ctx:c2llvmParser.ParamsInvokePatternContext):
        pass


    # Enter a parse tree produced by c2llvmParser#paramInvokePattern.
    def enterParamInvokePattern(self, ctx:c2llvmParser.ParamInvokePatternContext):
        pass

    # Exit a parse tree produced by c2llvmParser#paramInvokePattern.
    def exitParamInvokePattern(self, ctx:c2llvmParser.ParamInvokePatternContext):
        pass


    # Enter a parse tree produced by c2llvmParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:c2llvmParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by c2llvmParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:c2llvmParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by c2llvmParser#paramsDefinitionPattern.
    def enterParamsDefinitionPattern(self, ctx:c2llvmParser.ParamsDefinitionPatternContext):
        pass

    # Exit a parse tree produced by c2llvmParser#paramsDefinitionPattern.
    def exitParamsDefinitionPattern(self, ctx:c2llvmParser.ParamsDefinitionPatternContext):
        pass


    # Enter a parse tree produced by c2llvmParser#paramDefinitionPattern.
    def enterParamDefinitionPattern(self, ctx:c2llvmParser.ParamDefinitionPatternContext):
        pass

    # Exit a parse tree produced by c2llvmParser#paramDefinitionPattern.
    def exitParamDefinitionPattern(self, ctx:c2llvmParser.ParamDefinitionPatternContext):
        pass


    # Enter a parse tree produced by c2llvmParser#expression.
    def enterExpression(self, ctx:c2llvmParser.ExpressionContext):
        pass

    # Exit a parse tree produced by c2llvmParser#expression.
    def exitExpression(self, ctx:c2llvmParser.ExpressionContext):
        pass


    # Enter a parse tree produced by c2llvmParser#vType.
    def enterVType(self, ctx:c2llvmParser.VTypeContext):
        pass

    # Exit a parse tree produced by c2llvmParser#vType.
    def exitVType(self, ctx:c2llvmParser.VTypeContext):
        pass



del c2llvmParser