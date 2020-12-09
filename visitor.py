# Generated from c2llvm.g4 by ANTLR 4.9
from typing import Dict, List
from antlr4 import *
from llvmlite.ir.builder import IRBuilder
from llvmlite.ir.values import Block, Function
if __name__ is not None and "." in __name__:
    from .c2llvmParser import c2llvmParser
else:
    from c2llvmParser import c2llvmParser

from c2llvmVisitor import c2llvmVisitor
from llvmlite import ir

# This class defines a complete generic visitor for a parse tree produced by c2llvmParser.

double = ir.DoubleType()
int32 = ir.IntType(32)
int8 = ir.IntType(8)
void = ir.VoidType()

class Visitor(c2llvmVisitor):

    def __init__(self) -> None:
        super().__init__()
        self.module = ir.Module()
        self.module.triple = "x86_64-pc-linux-gnu"
        self.module.data_layout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
        self.scope = 0
        self.symbol_table:Dict[str,List[int]] = dict()

        self.functions:Dict[str,Function] = dict()
        self.blocks:List[Block] = []
        self.builders:List[IRBuilder] =[]

        self.local_vars = []
        self.current_func = ''


    # Visit a parse tree produced by c2llvmParser#prog.
    def visitProg(self, ctx:c2llvmParser.ProgContext):
        print("Prog")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#include.
    def visitInclude(self, ctx:c2llvmParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#declaration.
    def visitDeclaration(self, ctx:c2llvmParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#statement.
    def visitStatement(self, ctx:c2llvmParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#assignStatement.
    def visitAssignStatement(self, ctx:c2llvmParser.AssignStatementContext):
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
        if (len(self.blocks)==0):
            v_type = self.visit(ctx.getChild(0))
            


        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#funcStatement.
    def visitFuncStatement(self, ctx:c2llvmParser.FuncStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#paramsInvokePattern.
    def visitParamsInvokePattern(self, ctx:c2llvmParser.ParamsInvokePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#paramInvokePattern.
    def visitParamInvokePattern(self, ctx:c2llvmParser.ParamInvokePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:c2llvmParser.FunctionDeclarationContext):
        print("Function Declaration")

        self.enter_scope()

        return_type = self.visit(ctx.getChild(0))
        func_name = ctx.getChild(1).getText()
        params = self.visit(ctx.getChild(3))

        params_type = [param['type'] for param in params]

        func_proto = ir.FunctionType(return_type,params_type)
        func = ir.Function(self.module,func_proto,name=func_name)
        
        for index in range(0,len(params)):
            func.args[index].name = params[index]['name']
        
        block = func.append_basic_block(name=func_name+'.body')
        builder = ir.IRBuilder(block)
        
        self.functions[func_name] = func
        self.blocks.append(block)
        self.builders.append(builder)

        local_var_list = {}
        for index in range(0,len(params)):
            tmp_var = builder.alloca(params[index]['type'])
            builder.store(func.args[index],tmp_var)
            local_var_list[params[index]['name']]={
                'type':params[index]['type'],
                'name':tmp_var
            }
        
        self.local_vars.append(local_var_list)
        self.current_func = func_name

        for index in range(6,len(ctx.getChildCount()-1)):
            self.visit(ctx.getChild(index))
        
        self.current_func = ""
        self.blocks.pop()
        self.builders.pop()
        self.local_vars.pop()
        self.leave_scope()

        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#paramsDefinitionPattern.
    def visitParamsDefinitionPattern(self, ctx:c2llvmParser.ParamsDefinitionPatternContext):
        return [self.visit(ctx.getChild(index * 2)) for \
            index in range(0,(len(ctx.getChildCount())+1)//2)]


    # Visit a parse tree produced by c2llvmParser#paramDefinitionPattern.
    def visitParamDefinitionPattern(self, ctx:c2llvmParser.ParamDefinitionPatternContext):
        v_type = self.visit(ctx.getChild(0))
        v_name = ctx.getChild(1).getText()
        self.insert_symbol_table(v_name)
        return {
            'type':v_type,
            'name':v_name
        }


    # Visit a parse tree produced by c2llvmParser#expression.
    def visitExpression(self, ctx:c2llvmParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vType.
    def visitVType(self, ctx:c2llvmParser.VTypeContext):
        text = ctx.getText()
        if text == 'int':
            return int32
        elif text == 'char':
            return int8
        elif text == 'double':
            return double
        elif text == 'void':
            return void
        else:
            print("VType Error")
            return void


    def enter_scope(self):
        self.scope += 1

    def leave_scope(self):
        for k in self.symbol_table:
            if(self.symbol_table[k][-1] == self.scope):
                self.symbol_table[k].pop(-1)

                if (len(self.symbol_table[k])==0):
                    del self.symbol_table[k]
        self.scope -= 1

    
    def insert_symbol_table(self,v_name):
        if not v_name in self.symbol_table:
            self.symbol_table[v_name] = [self.scope]
        elif self.symbol_table[v_name][-1] == self.scope:
            print("Redefinition Error: {}".format(v_name))
        else:
            self.symbol_table[v_name].append(self.scope)

del c2llvmParser