from antlr.coolParser import coolParser
from antlr.coolListener import coolListener
from util.exceptions import assignnoconform, badargs1, badarith, baddispatch, badequalitytest, badequalitytest2, badmethodcallsitself, badstaticdispatch, badwhilecond, letbadinit, outofscope
from util.structure import _allClasses
from util.utils import *

class semanticThreeListener(coolListener):
    def enterPrimary(self, ctx: coolParser.PrimaryContext):
        if ctx.ID():
            name = ctx.ID().getText()
            symbol_table = utils.getScope(ctx)
            current_klass = utils.getKlass(ctx)
            if name == 'self':
                ctx.type = current_klass.name
            else:
                if name in symbol_table:
                    ctx.type = symbol_table[name]
                else:
                    raise outofscope()
        if ctx.INTEGER():
            ctx.type = 'Int'
        elif ctx.STRING():
            ctx.type = 'String'
        elif ctx.TRUE() or ctx.FALSE():
            ctx.type = 'Bool'

    def exitPrimary(self, ctx: coolParser.PrimaryContext):
        if ctx.expr():
            ctx.type = ctx.expr().type

    def exitExpr_primary(self, ctx: coolParser.Expr_primaryContext):
        ctx.type = ctx.getChild(0).type

    def enterNew_type(self, ctx: coolParser.New_typeContext):
        klass_type = ctx.TYPE().getText()
        current_klass = utils.getKlass(ctx)
        if klass_type == 'SELF_TYPE':
            ctx.type = current_klass.name
        else:
            if type(ctx.parentCtx) is coolParser.PrimaryContext:
                ctx.type = klass_type
            else:
                up_klass = _allClasses[klass_type].lookupInheritance()
                ctx.type = klass_type if up_klass == 'Object' else up_klass

    def exitAssignment(self, ctx: coolParser.AssignmentContext):
        symbol_table = utils.getScope(ctx)
        current_klass = utils.getKlass(ctx)
        right_expr = ctx.expr()
        left_type = symbol_table[ctx.ID().getText()]
        right_type = 'Object'
        try:
            right_type = right_expr.type
        except:
            if type(right_expr) is coolParser.Method_callContext:
                right_type = current_klass.lookupMethod(right_expr.ID().getText()).type
        if left_type in _allClasses:
            l_klass = _allClasses[left_type]
        if right_type in _allClasses:
            r_klass = _allClasses[right_type]
        if not l_klass.conforms(r_klass):
            raise assignnoconform()

    def enterMethod(self, ctx: coolParser.MethodContext):
        ctx.symbol_table.openScope()
        for name, type in ctx.method.params.items():
            ctx.symbol_table[name] = type

    def exitMethod(self, ctx: coolParser.MethodContext):
        ctx.symbol_table.closeScope()

    def enterLet_in(self, ctx: coolParser.Let_inContext):
        symbol_table = utils.getScope(ctx)
        ctx.symbol_table = symbol_table
        ctx.symbol_table.openScope()
        for decl in ctx.let_decl():
            decl_id = decl.ID().getText()
            decl_type = decl.TYPE().getText()
            ctx.symbol_table[decl_id] = decl_type
    
    def exitLet_in(self, ctx: coolParser.Let_inContext):
        ctx.type = list(ctx.symbol_table.values())[-1]
        ctx.symbol_table.closeScope()

    def exitLet_decl(self, ctx: coolParser.Let_declContext):
        let_type = ctx.TYPE().getText()
        if ctx.expr():
            expr_type = ctx.expr().type
            if let_type != expr_type:
                raise letbadinit()

    def enterMethod_call(self, ctx: coolParser.Method_callContext):
        name = ctx.ID().getText()
        current_klass = utils.getKlass(ctx)
        try:
            method_lookup = _allClasses[current_klass.name].lookupMethod(name)
            ctx.type = method_lookup.type
        except KeyError:
            pass
        if len(ctx.params) > 0:
            for param in ctx.params:
                try:
                    paramName = param.ID().getText()
                except:
                    paramName = ''
                if paramName == name:
                    raise badmethodcallsitself()

    def exitWhile(self, ctx: coolParser.WhileContext):
        while_condition = ctx.expr(0)
        if while_condition.type != 'Bool':
            raise badwhilecond()

    def exitDispatch(self, ctx: coolParser.DispatchContext):
        symbol_table = utils.getScope(ctx)
        name = ctx.expr(0).getText()
        try:
            klass_type = symbol_table[name]
        except:
            klass_type = ctx.expr(0).type
        
        if ctx.TYPE():
            static_klass_type = ctx.TYPE().getText()
            if klass_type in _allClasses:
                l_klass = _allClasses[klass_type]
            if static_klass_type in _allClasses:
                r_klass = _allClasses[static_klass_type]
            if not r_klass.conforms(l_klass):
                if klass_type != static_klass_type:
                    raise badstaticdispatch()
                else:
                    klass_type = r_klass.name
        
        method_name = ctx.ID().getText()
        try:
            method_lookup = _allClasses[klass_type].lookupMethod(method_name)
        except KeyError:
            raise baddispatch()
        param_idx = 0
        for name in method_lookup.params:
            signature_klass = _allClasses[method_lookup.params[name]]
            input_klass = _allClasses[ctx.params[param_idx].type]
            if not signature_klass.conforms(input_klass):
                raise badargs1()
            param_idx += 1
        ctx.type = method_lookup.type

    def exitArith(self, ctx: coolParser.ArithContext):
        if ctx.expr(0).type != 'Int' or ctx.expr(1).type != 'Int':
            raise badarith()
        ctx.type = 'Int'

    def exitEquals(self, ctx: coolParser.EqualsContext):
        left = ctx.children[0].type
        right = ctx.children[2].type
        if left == 'Int':
            if right == 'String':
                raise badequalitytest()
            else:
                raise badequalitytest2()
        