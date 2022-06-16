# Generated from C:/Users/rodol/OneDrive/Desktop/Proyecto/cool/antlr\cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .coolParser import coolParser
else:
    from coolParser import coolParser

# This class defines a complete generic visitor for a parse tree produced by coolParser.

class coolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by coolParser#program.
    def visitProgram(self, ctx:coolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#klass.
    def visitKlass(self, ctx:coolParser.KlassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#feature_function.
    def visitFeature_function(self, ctx:coolParser.Feature_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#feature_attribute.
    def visitFeature_attribute(self, ctx:coolParser.Feature_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#formal.
    def visitFormal(self, ctx:coolParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#new_type.
    def visitNew_type(self, ctx:coolParser.New_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#dispatch.
    def visitDispatch(self, ctx:coolParser.DispatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#assignment.
    def visitAssignment(self, ctx:coolParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#expr_primary.
    def visitExpr_primary(self, ctx:coolParser.Expr_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#sum.
    def visitSum(self, ctx:coolParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#method_call.
    def visitMethod_call(self, ctx:coolParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#while.
    def visitWhile(self, ctx:coolParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#less_or_equal_than.
    def visitLess_or_equal_than(self, ctx:coolParser.Less_or_equal_thanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#content.
    def visitContent(self, ctx:coolParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#not.
    def visitNot(self, ctx:coolParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#case_of.
    def visitCase_of(self, ctx:coolParser.Case_ofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#is_void.
    def visitIs_void(self, ctx:coolParser.Is_voidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#w.
    def visitW(self, ctx:coolParser.WContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#less_than.
    def visitLess_than(self, ctx:coolParser.Less_thanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#equals.
    def visitEquals(self, ctx:coolParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#let_in.
    def visitLet_in(self, ctx:coolParser.Let_inContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#divide.
    def visitDivide(self, ctx:coolParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#multiply.
    def visitMultiply(self, ctx:coolParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#if_else.
    def visitIf_else(self, ctx:coolParser.If_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#substract.
    def visitSubstract(self, ctx:coolParser.SubstractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#case_stat.
    def visitCase_stat(self, ctx:coolParser.Case_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#let_decl.
    def visitLet_decl(self, ctx:coolParser.Let_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#primary.
    def visitPrimary(self, ctx:coolParser.PrimaryContext):
        return self.visitChildren(ctx)



del coolParser