from antlr.coolListener import coolListener
from antlr.coolParser import coolParser
from util.exceptions import *
from util.structure import *
from util.structure import _allClasses
from util.utils import *

class semanticTwoListener(coolListener):
    def enterKlass(self, ctx: coolParser.KlassContext):
        klasses_dict = utils.getKlasses(ctx)
        klass = ctx.TYPE(0).getText()
        non_defined_klasses = utils.getInheritanceNonDefined(klasses_dict, _allClasses, klass)
        while non_defined_klasses:
            name = non_defined_klasses.pop()
            inherits = klasses_dict[name]
            Klass(name, inherits)
        if klass in _allClasses:
            k = _allClasses[klass]
        else:
            k = Klass(klass, klasses_dict[klass])
        symbolTable = SymbolTableWithScopes(k)
        ctx.current_klass = k
        for feature in ctx.feature():
            feature.current_klass = k
            feature.symbol_table = symbolTable
        
    def enterAttribute(self, ctx: coolParser.AttributeContext):
        attr_name = ctx.ID().getText()
        attr_type = ctx.TYPE().getText()

        if ctx.expr():
            expr = ctx.expr()
            try:
                if expr.getChild(0).ID():
                    ctx.current_klass.lookupAttribute(expr.getText())
            except KeyError:
                raise attrbadinit()
            except:
                pass

        try:
            type_lookup = ctx.current_klass.lookupAttribute(attr_name)
            if attr_type != type_lookup:
                raise attroverride()
        except KeyError:
            ctx.current_klass.addAttribute(attr_name, attr_type)

    def enterMethod(self, ctx: coolParser.MethodContext):
        method_type = ctx.TYPE().getText()
        if method_type != 'SELF_TYPE' and method_type not in _allClasses:
            raise returntypenoexist()
        if method_type == 'SELF_TYPE':
            self.check_self_type_usage(ctx)
        params = []
        if len(ctx.params) > 0:
            for param in ctx.params:
                param_name = param.ID().getText()
                param_type = param.TYPE().getText()
                if any(param_name in param for param in params):
                    raise dupformals()
                params.append((param_name, param_type))
            method = Method(method_type, params=params)
        else:
            method = Method(method_type)
        name = ctx.ID().getText()
        try:
            method_lookup = ctx.current_klass.lookupMethod(name)
            if len(method_lookup.params) != len(method.params):
                raise signaturechange()
            elif list(method_lookup.params.values() != list(method.params.values())):
                raise overridingmethod4()
        except KeyError:
            ctx.current_klass.addMethod(name, method)
        ctx.method = method

    def check_self_type_usage(self, ctx: coolParser.MethodContext):
        child_count = ctx.expr().getChildCount()
        if child_count == 1:
            massive = ctx.expr().getChild(0).getText()
            if 'self' in massive or 'newSELF_TYPE' in massive:
                raise selftypebadreturn()
        else:
            for i in range(child_count-1, -1, -1):
                curr_expr = ctx.expre().getChild(i).getText()
                if curr_expr not in utils.terminal_symbols:
                     if curr_expr == 'self' or (curr_expr == 'SELF_TYPE' and ctx.expr().getChild(i-1).getText() == 'new'):
                        raise selftypebadreturn()

    def enterCase_stat(self, ctx: coolParser.Case_statContext):
        name = ctx.ID().getText()
        type = ctx.TYPE().getText()
        symbol_table = utils.getScope(ctx)
        if name not in symbol_table:
            symbol_table[name] = type

    def exitCase_of(self, ctx: coolParser.Case_ofContext):
        used_types = []
        for case_stat in ctx.case_stat():
            case_type = case_stat.TYPE().getText()
            if case_type in used_types:
                raise caseidenticalbranch()
            else:
                used_types.append(case_type)