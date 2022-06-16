from antlr.coolParser import coolParser
from antlr.coolListener import coolListener
from util.exceptions import *
from util.utils import *
from util.structure import *
from util.structure import _allClasses

class semanticOneListener(coolListener):
    def __init__(self):
        _allClasses.clear()
        setBaseKlasses()

    def enterProgram(self, ctx: coolParser.ProgramContext):
        self.add_basic_classes_to_symbol_table(ctx)

    def exitProgram(self, ctx: coolParser.ProgramContext):
        if 'Main' not in ctx.klasses_dict:
            raise nomain()
        for klass in ctx.klasses_dict:
            inherits = ctx.klasses_dict[klass]
            if inherits not in ctx.klasses_dict:
                raise missingclass()
        
    def enterKlass(self, ctx: coolParser.KlassContext):
        klass_type = ctx.TYPE(0).getText()
        klasses_dict = utils.getKlasses(ctx)
        self.check_klass_not_redefined(klass_type, klasses_dict)
        if ctx.TYPE(1):
            superklass_type = ctx.TYPE(1).getText()
            self.check_inherits_basic_classes(superklass_type)
            klasses_dict[klass_type] = superklass_type
        else:
            klasses_dict[klass_type] = 'Object'

    def enterAttribute(self, ctx: coolParser.AttributeContext):
        if ctx.ID().getText() == 'self':
            raise anattributenamedself()

    def enterAssignment(self, ctx: coolParser.AssignmentContext):
        if ctx.ID() and ctx.ID().getText() == 'self':
            raise selfassignment()
        
    def enterFormal(self, ctx: coolParser.FormalContext):
        if ctx.ID().getText() == 'self':
            raise selfinformalparameter()
        if ctx.TYPE().getText() == 'SELF_TYPE':
            raise selftypeparameterposition()
    
    def enterLet_decl(self, ctx: coolParser.Let_declContext):
        if ctx.ID().getText() == 'self':
            raise letself()

    def add_basic_classes_to_symbol_table(self, ctx: coolParser.ProgramContext):
        ctx.klasses_dict = SymbolTable()
        ctx.klasses_dict['Object'] = 'Object'
        ctx.klasses_dict['IO'] = 'Object'
        ctx.klasses_dict['Int'] = 'Object'
        ctx.klasses_dict['String'] = 'Object'
        ctx.klasses_dict['Bool'] = 'Object'
        
    def check_klass_not_redefined(self, klass_type, klasses_dict):
        if klass_type == 'Int':
            raise badredefineint()
        if klass_type == 'Object':
            raise redefinedobject()
        if klass_type == 'SELF_TYPE':
            raise selftyperedeclared()
        if klass_type in klasses_dict:
            raise redefinedclass

    def check_inherits_basic_classes(self, superklass_type):
        if superklass_type == 'Bool':
            raise inheritsbool()
        if superklass_type == 'SELF_TYPE':
            raise inheritsselftype()
        if superklass_type == 'String':
            raise inheritsstring()
