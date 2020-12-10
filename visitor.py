# Generated from c2llvm.g4 by ANTLR 4.9
from io import BufferedRandom
from typing import Dict, List
from antlr4 import *
from llvmlite.ir import builder
from llvmlite.ir.builder import IRBuilder
from llvmlite.ir.instructions import SelectInstr
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

        self.global_vars = {}


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

            index = 1
            total = ctx.getChildCount()

            while(index<total):
                v_name = ctx.getChild(index).getText()
                self.insert_symbol_table(v_name)

                tmp_var = ir.GlobalVariable(self.module,v_type,name=v_name)
                tmp_var.linkage = 'common'

                self.global_vars[v_name] = {
                    'type':v_type,
                    'name':tmp_var
                }

                has_assign = (ctx.getChild(index+1).getText()=='=')

                if has_assign:
                    self.visit(ctx.getChild(index+2))

                else:
                    index+=2
                

            


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


    # Visit a parse tree produced by c2llvmParser#Neg.
    def visitNeg(self, ctx:c2llvmParser.NegContext):
        res = self.visit(ctx.getChild(1))
        res = self.toBool(res)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#MulDivMod.
    def visitMulDivMod(self, ctx:c2llvmParser.MulDivModContext):
        builder = self.builders[-1]
        lres = self.visit(ctx.getChild(0))
        rres = self.visit(ctx.getChild(2))

        lres,rres = self.convertToSameType(lres,rres)

        tmp_var =None

        if ctx.getChild(1).getText() == '*':
            tmp_var = builder.mul(lres['name'],rres['name'])
        elif ctx.getChild(1).getText() == '/':
            tmp_var = builder.sdiv(lres['name'],rres['name'])
        elif ctx.getChild(1).getText() =='%':
            tmp_var  = builder.srem(lres['name'],rres['name'])
        else:
            print("MulDivMod Error")
        return {
            'type':lres['type'],
            'const':False,
            'name':tmp_var
        }


    # Visit a parse tree produced by c2llvmParser#FunctionExpr.
    def visitFunctionExpr(self, ctx:c2llvmParser.FunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#Or.
    def visitOr(self, ctx:c2llvmParser.OrContext):
        lres = self.visit(ctx.getChild(0))
        lres = self.toBool(lres)
        rres = self.visit(ctx.getChild(2))
        rres = self.toBool(rres)
        builder = self.builders[-1]
        res = builder.or_(lres['name'],rres['name'])
        
        return {
            'type':lres['type'],
            'const':False,
            'name':res
        }


    # Visit a parse tree produced by c2llvmParser#Parens.
    def visitParens(self, ctx:c2llvmParser.ParensContext):
        return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by c2llvmParser#Char.
    def visitChar(self, ctx:c2llvmParser.CharContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by c2llvmParser#And.
    def visitAnd(self, ctx:c2llvmParser.AndContext):
        lres = self.visit(ctx.getChild(0))
        lres = self.toBool(lres)
        rres = self.visit(ctx.getChild(2))
        rres = self.toBool(rres)
        builder = self.builders[-1]

        res = builder.and_(lres['name'],rres['name'])
        return {
            'type':lres['type'],
            'const':False,
            'name':res
        }


    # Visit a parse tree produced by c2llvmParser#Compare.
    def visitCompare(self, ctx:c2llvmParser.CompareContext):
        builder = self.builders[-1]
        lres = self.visit(ctx.getChild(0))
        rres = self.visit(ctx.getChild(2))

        lres,rres = self.convertToSameType(lres,rres)
        op = ctx.getChild(1).getText()

        tmp_var = None

        if lres['type'] == double:
            tmp_var = builder.fcmp_ordered(op,lres['name'],rres['name'])
        elif self.isInteger(lres):
            tmp_var  = builder.icmp_signed(op,lres['name'],rres['name'])
        else:
            print("Compare Error")
        return {
            'type':int8,
            'const':False,
            'name':tmp_var
        }




    # Visit a parse tree produced by c2llvmParser#Id.
    def visitId(self, ctx:c2llvmParser.IdContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by c2llvmParser#Double.
    def visitDouble(self, ctx:c2llvmParser.DoubleContext):
        if ctx.getChild(0).getText() == '-':
            res = self.visit(ctx.getChild(1))
            builder = self.builders[-1]
            tmp_var = builder.neg(res['name'])
            return {
                'type':res['type'],
                'name':tmp_var
            }
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by c2llvmParser#Int.
    def visitInt(self, ctx:c2llvmParser.IntContext):
        if ctx.getChild(0).getText() == '-':
            res = self.visit(ctx.getChild(1))
            builder = self.builders[-1]
            tmp_var = builder.neg(res['name'])
            return {
                'type':res['type'],
                'name':tmp_var
            }
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by c2llvmParser#AndSub.
    def visitAddSub(self, ctx:c2llvmParser.AddSubContext):
        builder = self.builders[-1]
        lres = self.visit(ctx.getChild(0))
        rres = self.visit(ctx.getChild(2))

        lres,rres = self.convertToSameType(lres,rres)

        tmp_var =None

        if ctx.getChild(1).getText() == '+':
            tmp_var =builder.add(lres['name'],rres['name'])
        elif ctx.getChild(1).getText() =='-':
            tmp_var = builder.sub(lres['name'],rres['name'])
        else:
            print("AddSub Error")
        return {
            'type':lres['type'],
            'const':False,
            'name':tmp_var
        }


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

        # Visit a parse tree produced by c2llvmParser#vInt.
    def visitVInt(self, ctx:c2llvmParser.VIntContext):
        return {
            'type':int32,
            'const':True,
            'name':ir.Constant(int32,int(ctx.getText()))
        }
        


    # Visit a parse tree produced by c2llvmParser#vChar.
    def visitVChar(self, ctx:c2llvmParser.VCharContext):
        return {
            'type':int8,
            'const':True,
            'name':ir.Constant(int8,ord(ctx.getText()[1]))
        }


    # Visit a parse tree produced by c2llvmParser#vDouble.
    def visitVDouble(self, ctx:c2llvmParser.VDoubleContext):
        return {
            'type':double,
            'const':True,
            'name':ir.Constant(double,float(ctx.getText()))
        }


    # Visit a parse tree produced by c2llvmParser#vString.
    def visitVString(self, ctx:c2llvmParser.VStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#vId.
    def visitVId(self, ctx:c2llvmParser.VIdContext):
        v_name = ctx.getText()
        if not self.check_var_define(v_name):
            return {
                'type':int32,
                'const':False,
                'name':ir.Constant(int32,0)
            }
        builder = self.builders[-1]
        


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
    
    def check_var_define(self,v_name):
        if not v_name in self.symbol_table:
            print("Check Var Define Error")
            return False,
        if self.symbol_table[v_name][0]< self.scope:
            print("Check Var Define Error")
            return False
        return True
    
    def toBool(self,res,flag = 0):
        op = '=='
        if flag:
            op = '!='
        
        builder = self.builders[-1]
        if res['type'] == int8 or res['type']==int32:
            tmp_var = builder.icmp_signed(op,res['name'],ir.Constant(res['type'],0))
            return {
                'type': int8,
                'constant':False,
                'name':tmp_var
            }
        elif res['type']==double:
            tmp_var = builder.fcmp_ordered(op,res['name'],ir.Constant(res['type'],0))
            return {
                'type':int8,
                'constant':False,
                'name':tmp_var
            }
        else:
            print("toBool Error")
            return res
    
    def isInteger(self,res):
        return res['type'] == int32 or res['type']==int8

    def isDouble(self,res):
        return res['type'] == double

    def convertToType(self,res,dtype):
        builder = self.builders[-1]

        if dtype == int32 or dtype == int8:
            tmp_var = builder.sext(res['name'],dtype)
            return {
                'type':dtype,
                'const':False,
                'name':tmp_var
            }
        elif dtype == double:
            tmp_var  = builder.sitofp(res['name'],dtype)
            return {
                'type':dtype,
                'const':False,
                'name':tmp_var
            }
        else:
            print("ConvertToType Error")

    def convertToSameType(self,lres,rres):
        if lres['type'] == rres['type']:
            return lres,rres
        if self.isInteger(lres) and self.isInteger(rres):
            if lres['type'].width < rres['type'].width:
                lres = self.convertToType(lres,rres['type'])
            else:
                rres = self.convertToType(rres,lres['type'])
        
        elif self.isInteger(lres) and self.isDouble(rres):
            lres = self.convertToType(lres,rres['type'])
        elif self.isInteger(rres) and self.isDouble(lres):
            rres = self.convertToType(rres,lres['type'])
        else:
            print("ConvertToSameType Error")
        return lres,rres
        
        

del c2llvmParser