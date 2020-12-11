# Generated from c2llvm.g4 by ANTLR 4.9
from os import O_NDELAY, name
from typing import Dict, List
from antlr4 import *
from llvmlite.ir import builder
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
int1 = ir.IntType(1)
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

        self.need_load = True

        self.structures  = dict()

        self.end_condition_block = None

        self.vstring_num = 0

        self.init_internal_functions()

    def init_internal_functions(self):
        printfty = ir.FunctionType(int32,[ir.PointerType(int8)],var_arg=True)
        printf = ir.Function(self.module,printfty,name="printf")
        self.functions['printf']= printf

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
        self.enter_scope()

        struct_name = ctx.getChild(0).getChild(1).getText()
        if struct_name in self.structures:
            print("Struct Declaration Error")
            return
        
        member_types = []
        member_names = []
        for index in range(2,ctx.getChildCount()-2):
            v_types,v_names = self.visit(ctx.getChild(index))
            member_types.extend(v_types)
            member_names.extend(v_names)
        
        self.structures[struct_name]={
            'members':member_names,
            'struct':ir.LiteralStructType(member_types)
        }
        self.leave_scope()


    # Visit a parse tree produced by c2llvmParser#structMemberDeclaration.
    def visitStructMemberDeclaration(self, ctx:c2llvmParser.StructMemberDeclarationContext):
        v_types = []
        v_names = []

        if ctx.getChild(0).getChildCount() == 1:
            v_type = self.visit(ctx.getChild(0))

            for index in range(0,(ctx.getChildCount() - 1) // 2):
                if ctx.getChild(2*index+1).getChildCount() == 1:
                    v_names.append(ctx.getChild(2*index+1).getText())
                    v_types.append(v_type)
                elif ctx.getChild(2*index+1).getChildCount() == 4:
                    res = self.visit(ctx.getChild(2*index+1))
                    v_names.append(res['name'])
                    v_types.append(ir.ArrayType(v_type,res['length']))
                else:
                    print("Struct Member Declaration Error")
        
        else:
            print("Error")


    # Visit a parse tree produced by c2llvmParser#statement.
    def visitStatement(self, ctx:c2llvmParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#assignStatement.
    def visitAssignStatement(self, ctx:c2llvmParser.AssignStatementContext):
        builder = self.builders[-1]

        res = self.visit(ctx.getChild(ctx.getChildCount()-2))

        for index in reversed(range(0,(ctx.getChildCount() - 2)//2 )):
            need_load_backup = self.need_load
            self.need_load = False

            v_res = self.visit(ctx.getChild(index*2))
            self.need_load=need_load_backup

            res = self.convertToType(res,v_res['type'])
            builder.store(res['name'],v_res['name'])

            tmp_var = builder.load(v_res['name'])
            res = {
                'type':v_res['type'],
                'const':False,
                'name':tmp_var
            }
        
        return res


     # Visit a parse tree produced by c2llvmParser#conditionStatement.
    def visitConditionStatement(self, ctx:c2llvmParser.ConditionStatementContext):
        builder = self.builders[-1]

        condition_block = builder.append_basic_block()
        end_condition_block = builder.append_basic_block()
        builder.branch(condition_block)

        self.blocks.pop()
        self.builders.pop()
        self.blocks.append(condition_block)

        builder = ir.IRBuilder(condition_block)
        self.builders.append(builder)

        end_condition_block_backup = self.end_condition_block
        self.end_condition_block = end_condition_block
        
        self.visitChildren(ctx)

        self.end_condition_block = end_condition_block_backup

        block = self.blocks.pop()
        builder = self.builders.pop()

        if not block.is_terminated:
            builder.branch(end_condition_block)
        
        self.blocks.append(end_condition_block)
        self.builders.append(ir.IRBuilder(end_condition_block))

        return
    
    # Visit a parse tree produced by c2llvmParser#ifStatement.
    def visitIfStatement(self, ctx:c2llvmParser.IfStatementContext):
        self.enter_scope()
        res = self.visit(ctx.getChild(2))
        builder = self.builders[-1]

        if_true_block = builder.append_basic_block()
        if_false_block = builder.append_basic_block()
        res = self.toBool(res)
        builder.cbranch(res['name'],if_true_block,if_false_block)

        self.blocks.pop()
        self.builders.pop()

        self.blocks.append(if_true_block)
        self.builders.append(ir.IRBuilder(if_true_block))
        self.local_vars.append({})
        
        for index in range(5,ctx.getChildCount()-1):
            self.visit(ctx.getChild(index))
        
        if not self.blocks[-1].is_terminated:
            builder = self.builders[-1]
            builder.branch(self.end_condition_block)
        
        self.blocks.pop()
        self.builders.pop()
        self.local_vars.pop()

        self.blocks.append(if_false_block)
        self.builders.append(ir.IRBuilder(if_false_block))
        self.leave_scope()
        return



    # Visit a parse tree produced by c2llvmParser#elseifStatement.
    def visitElseifStatement(self, ctx:c2llvmParser.ElseifStatementContext):
        self.enter_scope()
        res = self.visit(ctx.getChild(3))
        builder = self.builders[-1]

        elseif_true_block = builder.append_basic_block()
        elseif_false_block = builder.append_basic_block()

        res = self.toBool(res)
        builder.cbranch(res['name'],elseif_true_block,elseif_false_block)

        self.blocks.pop()
        self.builders.pop()

        self.blocks.append(elseif_true_block)
        self.builders.append(ir.IRBuilder(elseif_true_block))
        self.local_vars.append({})

        for index in range(6,ctx.getChildCount()-1):
            self.visit(ctx.getChild(index))
        
        if not self.blocks[-1].is_terminated:
            builder=self.builders[-1]
            builder.branch(self.end_condition_block)
        
        self.blocks.pop()
        self.builders.pop()
        self.local_vars.pop()

        self.blocks.append(elseif_false_block)
        self.builders.append(ir.IRBuilder(elseif_false_block))
        self.leave_scope()
        return



    # Visit a parse tree produced by c2llvmParser#elseStatement.
    def visitElseStatement(self, ctx:c2llvmParser.ElseStatementContext):
        self.enter_scope()
        self.local_vars.append({})

        for index in range(2,ctx.getChildCount()-1):
            self.visit(ctx.getChild(index))
        
        self.local_vars.pop()
        self.leave_scope()
        return


    # Visit a parse tree produced by c2llvmParser#whileStatement.
    def visitWhileStatement(self, ctx:c2llvmParser.WhileStatementContext):
        self.enter_scope()
        builder = self.builders[-1]
        while_condition_block = builder.append_basic_block()
        while_body_block = builder.append_basic_block()
        while_end_block = builder.append_basic_block()

        builder.branch(while_condition_block)

        self.blocks.pop()
        self.builders.pop()

        self.blocks.append(while_condition_block)
        self.builders.append(ir.IRBuilder(while_condition_block))

        res = self.visit(ctx.getChild(2))
        res = self.toBool(res)

        builder = self.builders[-1]
        builder.cbranch(res['name'],while_body_block,while_end_block)

        self.blocks.pop()
        self.builders.pop()

        self.blocks.append(while_body_block)
        self.builders.append(ir.IRBuilder(while_body_block))
        self.local_vars.append({})

        for index in range(5,ctx.getChildCount()-1):
            self.visit(ctx.getChild(index))
        
        builder = self.builders[-1]
        builder.branch(while_condition_block)
        self.blocks.pop()
        self.builders.pop()
        self.local_vars.pop()

        self.blocks.append(while_end_block)
        self.builders.append(ir.IRBuilder(while_end_block))
        self.leave_scope()
        return



    # Visit a parse tree produced by c2llvmParser#forStatement.
    def visitForStatement(self, ctx:c2llvmParser.ForStatementContext):
        self.enter_scope()
        self.visit(ctx.getChild(2))

        builder = self.builders[-1]
        for_condition_block = builder.append_basic_block()
        for_body_block = builder.append_basic_block()
        for_end_block = builder.append_basic_block()

        builder.branch(for_condition_block)

        self.blocks.pop()
        self.builders.pop()
        self.blocks.append(for_condition_block)
        self.builders.append(ir.IRBuilder(for_condition_block))

        res = self.visit(ctx.getChild(4))
        res = self.toBool(res)

        builder = self.builders[-1]
        builder.cbranch(res['name'],for_body_block,for_end_block)

        self.blocks.pop()
        self.builders.pop()

        self.blocks.append(for_body_block)
        self.builders.append(ir.IRBuilder(for_body_block))
        self.local_vars.append({})

        for index in range(9,ctx.getChildCount()-1):
            self.visit(ctx.getChild(index))
        
        self.visit(ctx.getChild(6))

        builder = self.builders[-1]
        builder.branch(for_condition_block)
        self.blocks.pop()
        self.builders.pop()
        self.local_vars.pop()

        self.blocks.append(for_end_block)
        self.builders.append(ir.IRBuilder(for_end_block))
        self.leave_scope()
        return




    # Visit a parse tree produced by c2llvmParser#forInitStatement.
    def visitForInitStatement(self, ctx:c2llvmParser.ForInitStatementContext):
        if ctx.getChildCount()==0:
            return
        
        need_load_backup = self.need_load
        self.need_load = False
        
        v_res = self.visit(ctx.getChild(0))
        self.need_load = need_load_backup

        expr_res = self.visit(ctx.getChild(2))
        expr_res =  self.convertToType(expr_res,v_res['type'])

        builder = self.builders[-1]
        builder.store(expr_res['name'],v_res['name'])

        if ctx.getChildCount() >=5:
            self.visit(ctx.getChild(4))



    # Visit a parse tree produced by c2llvmParser#forExecStatement.
    def visitForExecStatement(self, ctx:c2llvmParser.ForExecStatementContext):
        if ctx.getChildCount()==0:
            return
        
        need_load_backup = self.need_load
        self.need_load = False
        v_res = self.visit(ctx.getChild(0))
        self.need_load = need_load_backup

        expr_res = self.visit(ctx.getChild(2))
        expr_res = self.convertToType(expr_res,v_res['type'])

        builder = self.builders[-1]
        builder.store(expr_res['name'],v_res['name'])

        if ctx.getChildCount()>=5:
            self.visit(ctx.getChild(4))
        return




    # Visit a parse tree produced by c2llvmParser#returnStatement.
    def visitReturnStatement(self, ctx:c2llvmParser.ReturnStatementContext):
        builder = self.builders[-1]

        if ctx.getChildCount()==2:
            ret = builder.ret_void()
            return {
                'type':void,
                'const':False,
                'name':ret
            }
        
        res = self.visit(ctx.getChild(1))
        ret = builder.ret(res['name'])
        return {
            'type':ret.type,
            'const':False,
            'name':ret
        }

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

    # Visit a parse tree produced by c2llvmParser#arrayDefinitionStatement.
    def visitArrayDefinitionStatement(self, ctx:c2llvmParser.ArrayDefinitionStatementContext):
        v_type = self.visit(ctx.getChild(0))
        v_name = ctx.getChild(1).getText()
        array_len = int(ctx.getChild(3).getText())

        if len(self.blocks) == 0:
            self.insert_symbol_table(v_name)
            if v_name in self.global_vars:
                print("Error")
            tmp_var = ir.GlobalVariable(self.module,ir.ArrayType(v_type,array_len))
            tmp_var.linkage = 'common'
            self.global_vars[v_name]={
                'type':ir.ArrayType(v_type,array_len),
                'name':tmp_var
            }
            return
        
        builder = self.builders[-1]
        local_var_list = self.local_vars[-1]
        self.insert_symbol_table(v_name)
        if v_name in self.local_vars:
            print("Error")
            return 
        tmp_var = builder.alloca(ir.ArrayType(v_type,array_len),name=v_name)
        local_var_list[v_name]={
            'type':ir.ArrayType(v_type,array_len),
            'name':tmp_var
        }
        return



    # Visit a parse tree produced by c2llvmParser#structDefinitionStatement.
    def visitStructDefinitionStatement(self, ctx:c2llvmParser.StructDefinitionStatementContext):
        res = self.visit(ctx.getChild(0))
        v_type = res['struct']
        struct_name = ctx.getChild(0).getChild(1).getText()

        if ctx.getChild(1).getChildCount() == 1:
            v_name = ctx.getChild(1).getText()
            self.insert_symbol_table(v_name)
            if len(self.blocks)==0:
                if v_name in self.global_vars:
                    print("Error")
                tmp_var = ir.GlobalVariable(self.module,v_type,name=v_name)
                tmp_var.linkage = 'common'
                tmp_var.initializer = ir.Constant(v_type,None)

                self.global_vars[v_name]={
                    'struct_name':struct_name,
                    'type':v_type,
                    'name':tmp_var
                }
            else:
                builder = self.builders[-1]
                local_var_list = self.local_vars[-1]
                if v_name in local_var_list:
                    print("Error")
                tmp_var = builder.alloca(v_type,name=v_name)
                local_var_list[v_name]={
                    'struct_name':struct_name,
                    'type':v_type,
                    'name':tmp_var
                }
        else:
            res = self.visit(ctx.getChild(1))
            v_name = res['name']

            v_type = ir.ArrayType(v_type,res['length'])
            self.insert_symbol_table(v_name)

            if len(self.blocks)==0:
                if v_name in self.global_vars:
                    print("Error")
                tmp_var = ir.GlobalVariable(self.module,v_type,name=v_name)
                tmp_var.linkage = 'common'
                tmp_var.initializer = ir.Constant(v_type,None)

                self.global_vars[v_name]={
                    'struct_name':struct_name,
                    'type':v_type,
                    'name':tmp_var
                }
            else:
                builder = self.builders[-1]
                local_var_list = self.local_vars[-1]

                if v_name in local_var_list:
                    print("Error")
                tmp_var = builder.alloca(v_type,name=v_name)
                local_var_list[v_name]={
                    'struct_name':struct_name,
                    'type':v_type,
                    'name':tmp_var
                }
        return
            


    # Visit a parse tree produced by c2llvmParser#vArrayItem.
    def visitVArrayItem(self, ctx:c2llvmParser.VArrayItemContext):
        need_load_backup = self.need_load
        self.need_load = False
        res = self.visit(ctx.getChild(0))
        self.need_load = need_load_backup

        if isinstance(res['type'],ir.types.ArrayType):
            builder = self.builders[-1]

            need_load_backup = self.need_load
            self.need_load = True
            index_res = self.visit(ctx.getChild(2))
            self.need_load = need_load_backup

            zero_base = ir.Constant(int32,0)
            tmp_var = builder.gep(res['name'],[zero_base,index_res['name']],inbounds=True)

            if self.need_load:
                tmp_var = builder.load(tmp_var)
            
            return {
                'type':res['type'].element,
                'const':False,
                'name':tmp_var,
                'struct_name':res['struct_name'] if 'struct_name' in res else None
            }
        else:
            pass


    # Visit a parse tree produced by c2llvmParser#vStructMember.
    def visitVStructMember(self, ctx:c2llvmParser.VStructMemberContext):
        builder = self.builders[-1]
        if ctx.getChild(0).getChildCount() == 1:
            if ctx.getChild(2).getChildCount()==1:
                need_loca_backup = self.need_load
                self.need_load = False
                res = self.visit(ctx.getChild(0))
                self.need_load = need_loca_backup

                struct_name = res['struct_name']
                index =self.structures[struct_name]['members'].index(ctx.getChild(2).getText())

                zero_base = ir.Constant(int32,0)
                offset = ir.Constant(int32,index)

                tmp_var = builder.gep(res['name'],[zero_base,offset],inbounds=True)

                if self.need_load:
                    tmp_var = builder.load(tmp_var)
                
                return {
                    'type':self.structures[struct_name]['struct'].elements[index],
                    'const':False,
                    'name':tmp_var
                }
            else:
                pass
            
        else:
            if ctx.getChild(2).getChildCount()==1:
                need_load_backup = self.need_load
                self.need_load = False
                res = self.visit(ctx.getChild(0))
                self.need_load = need_load_backup

                struct_name = res['struct_name']
                index = self.structures[struct_name]['members'].index(ctx.getChild(2).getText())
                zero_base = ir.Constant(int32,0)
                offset = ir.Constant(int32,index)
                tmp_var = builder.gep(res['name'],[zero_base,offset],inbounds=True)

                if self.need_load:
                    tmp_var = builder.load(tmp_var)
                
                return {
                    'type':self.structures[struct_name]['struct'].elements[index],
                    'const':False,
                    'name':tmp_var
                }
            else:
                pass

    # Visit a parse tree produced by c2llvmParser#funcStatement.
    def visitFuncStatement(self, ctx:c2llvmParser.FuncStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c2llvmParser#funcExpression.
    def visitFuncExpression(self, ctx:c2llvmParser.FuncExpressionContext):
        func_name = ctx.getChild(0).getText()

        # check inter function

        if func_name=='printf':
            printf = self.functions['printf']
        
            builder = self.builders[-1]
            zero_base = ir.Constant(int32,0)

            args = self.visit(ctx.getChild(2))
            args[0] = builder.gep(args[0]['name'],[zero_base,zero_base],inbounds=True)
            ret = builder.call(printf,args)
            
            return {
                'type':int32,
                'const':False,
                'name':ret
            }
        
        builder = self.builders[-1]

        if func_name in self.functions:
            func = self.functions[func_name]

            params = self.visit(ctx.getChild(2))

            for index in range(0,len(params)):
                params[index] = self.convertToType(params[index],func.args[index].type)
            
            params = list(map(lambda param:param['name'],params))

            tmp_var = builder.call(func,params)
            return {
                'type':func.function_type.return_type,
                'const':False,
                'name':tmp_var
            }
        else:
            print("Func Expression Error")




    # Visit a parse tree produced by c2llvmParser#paramsInvokePattern.
    def visitParamsInvokePattern(self, ctx:c2llvmParser.ParamsInvokePatternContext):
        return [self.visit(ctx.getChild(index)) for index in range(0,ctx.getChildCount(),2)]


    # Visit a parse tree produced by c2llvmParser#paramInvokePattern.
    def visitParamInvokePattern(self, ctx:c2llvmParser.ParamInvokePatternContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by c2llvmParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:c2llvmParser.FunctionDeclarationContext):

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

        for index in range(6,ctx.getChildCount()-1):
            self.visit(ctx.getChild(index))
        
        self.current_func = ""
        self.blocks.pop()
        self.builders.pop()
        self.local_vars.pop()
        self.leave_scope()

        return


    # Visit a parse tree produced by c2llvmParser#paramsDefinitionPattern.
    def visitParamsDefinitionPattern(self, ctx:c2llvmParser.ParamsDefinitionPatternContext):
        return [self.visit(ctx.getChild(index * 2)) for \
            index in range(0,(ctx.getChildCount()+1)//2)]


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
        return self.visit(ctx.getChild(0))


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
        v_string = ctx.getText().replace('\\n','\n')
        v_string = v_string[1:-1]
        v_string += '\0'
        v_len = len(bytearray(v_string,'utf-8'))

        self.vstring_num+=1
        v_name = ir.GlobalVariable(self.module,ir.ArrayType(int8,v_len),".string{}".format(self.vstring_num))
        v_name.global_constant = True
        v_name.initializer = ir.Constant(ir.ArrayType(int8,v_len),bytearray(v_string,'utf-8'))
        return {
            'type':ir.ArrayType(int8,v_len),
            'const':True,
            'name':v_name
        }


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

        for local_var_list in self.local_vars.reverse():
            if v_name in local_var_list:
                if self.need_load:
                    tmp_var = builder.load(local_var_list[v_name]['name'])
                    return {
                        'type':local_var_list[v_name]['type'],
                        'const':False,
                        'name':tmp_var,
                        'struct_name': local_var_list[v_name]['struct_name'] if 'struct_name' in local_var_list[v_name] else None
                    }
                else:
                    return {
                        'type':local_var_list[v_name]['type'],
                        'const':False,
                        'name':local_var_list[v_name]['name'],
                        'struct_name': local_var_list[v_name]['struct_name'] if 'struct_name' in local_var_list[v_name] else None
                    }

        if v_name in self.global_vars:
            if self.need_load:
                tmp_var = builder.load(self.global_vars[v_name]['name'])  
                return {
                    'type':self.global_vars[v_name]['type'],
                    'const':False,
                    'name':tmp_var,
                    'struct_name':self.global_vars[v_name]['struct_name'] if 'struct_name' in self.global_vars[v_name] else None
                }
            else:
                return {
                    'type':self.global_vars[v_name]['type'],
                    'const':False,
                    'name':self.global_vars[v_name]['name'],
                    'struct_name':self.global_vars[v_name]['struct_name'] if 'struct_name' in self.global_vars[v_name] else None
                }
        return {
            'type':void,
            'const':False,
            'name':ir.Constant(void,None)
        }

    # Visit a parse tree produced by c2llvmParser#vStruct.
    def visitVStruct(self, ctx:c2llvmParser.VStructContext):
        return self.structures[ctx.getChild(1).getText()]

    # Visit a parse tree produced by c2llvmParser#vArray.
    def visitVArray(self, ctx:c2llvmParser.VArrayContext):
        return {
            'name':ctx.getChild(0).getText(),
            'length':int(ctx.getChild(2).getText())
        }


    def enter_scope(self):
        self.scope += 1

    def leave_scope(self):
        for k in self.symbol_table:
            if(self.symbol_table[k][-1] == self.scope):
                self.symbol_table[k].pop(-1)

        for k in list(self.symbol_table.keys()):
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
                'type': int1,
                'constant':False,
                'name':tmp_var
            }
        elif res['type']==double:
            tmp_var = builder.fcmp_ordered(op,res['name'],ir.Constant(res['type'],0))
            return {
                'type':int1,
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