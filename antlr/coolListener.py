# Generated from C:/Users/rodol/OneDrive/Desktop/Proyecto/cool/antlr\cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .coolParser import coolParser
else:
    from coolParser import coolParser

# This class defines a complete listener for a parse tree produced by coolParser.
class coolListener(ParseTreeListener):

    # Enter a parse tree produced by coolParser#program.
    def enterProgram(self, ctx:coolParser.ProgramContext):
        pass

    # Exit a parse tree produced by coolParser#program.
    def exitProgram(self, ctx:coolParser.ProgramContext):
        pass


    # Enter a parse tree produced by coolParser#klass.
    def enterKlass(self, ctx:coolParser.KlassContext):
        pass

    # Exit a parse tree produced by coolParser#klass.
    def exitKlass(self, ctx:coolParser.KlassContext):
        pass


    # Enter a parse tree produced by coolParser#feature_function.
    def enterFeature_function(self, ctx:coolParser.Feature_functionContext):
        pass

    # Exit a parse tree produced by coolParser#feature_function.
    def exitFeature_function(self, ctx:coolParser.Feature_functionContext):
        pass


    # Enter a parse tree produced by coolParser#feature_attribute.
    def enterFeature_attribute(self, ctx:coolParser.Feature_attributeContext):
        pass

    # Exit a parse tree produced by coolParser#feature_attribute.
    def exitFeature_attribute(self, ctx:coolParser.Feature_attributeContext):
        pass


    # Enter a parse tree produced by coolParser#formal.
    def enterFormal(self, ctx:coolParser.FormalContext):
        pass

    # Exit a parse tree produced by coolParser#formal.
    def exitFormal(self, ctx:coolParser.FormalContext):
        pass


    # Enter a parse tree produced by coolParser#new_type.
    def enterNew_type(self, ctx:coolParser.New_typeContext):
        pass

    # Exit a parse tree produced by coolParser#new_type.
    def exitNew_type(self, ctx:coolParser.New_typeContext):
        pass


    # Enter a parse tree produced by coolParser#dispatch.
    def enterDispatch(self, ctx:coolParser.DispatchContext):
        pass

    # Exit a parse tree produced by coolParser#dispatch.
    def exitDispatch(self, ctx:coolParser.DispatchContext):
        pass


    # Enter a parse tree produced by coolParser#assignment.
    def enterAssignment(self, ctx:coolParser.AssignmentContext):
        pass

    # Exit a parse tree produced by coolParser#assignment.
    def exitAssignment(self, ctx:coolParser.AssignmentContext):
        pass


    # Enter a parse tree produced by coolParser#expr_primary.
    def enterExpr_primary(self, ctx:coolParser.Expr_primaryContext):
        pass

    # Exit a parse tree produced by coolParser#expr_primary.
    def exitExpr_primary(self, ctx:coolParser.Expr_primaryContext):
        pass


    # Enter a parse tree produced by coolParser#sum.
    def enterSum(self, ctx:coolParser.SumContext):
        pass

    # Exit a parse tree produced by coolParser#sum.
    def exitSum(self, ctx:coolParser.SumContext):
        pass


    # Enter a parse tree produced by coolParser#method_call.
    def enterMethod_call(self, ctx:coolParser.Method_callContext):
        pass

    # Exit a parse tree produced by coolParser#method_call.
    def exitMethod_call(self, ctx:coolParser.Method_callContext):
        pass


    # Enter a parse tree produced by coolParser#while.
    def enterWhile(self, ctx:coolParser.WhileContext):
        pass

    # Exit a parse tree produced by coolParser#while.
    def exitWhile(self, ctx:coolParser.WhileContext):
        pass


    # Enter a parse tree produced by coolParser#less_or_equal_than.
    def enterLess_or_equal_than(self, ctx:coolParser.Less_or_equal_thanContext):
        pass

    # Exit a parse tree produced by coolParser#less_or_equal_than.
    def exitLess_or_equal_than(self, ctx:coolParser.Less_or_equal_thanContext):
        pass


    # Enter a parse tree produced by coolParser#content.
    def enterContent(self, ctx:coolParser.ContentContext):
        pass

    # Exit a parse tree produced by coolParser#content.
    def exitContent(self, ctx:coolParser.ContentContext):
        pass


    # Enter a parse tree produced by coolParser#not.
    def enterNot(self, ctx:coolParser.NotContext):
        pass

    # Exit a parse tree produced by coolParser#not.
    def exitNot(self, ctx:coolParser.NotContext):
        pass


    # Enter a parse tree produced by coolParser#case_of.
    def enterCase_of(self, ctx:coolParser.Case_ofContext):
        pass

    # Exit a parse tree produced by coolParser#case_of.
    def exitCase_of(self, ctx:coolParser.Case_ofContext):
        pass


    # Enter a parse tree produced by coolParser#is_void.
    def enterIs_void(self, ctx:coolParser.Is_voidContext):
        pass

    # Exit a parse tree produced by coolParser#is_void.
    def exitIs_void(self, ctx:coolParser.Is_voidContext):
        pass


    # Enter a parse tree produced by coolParser#w.
    def enterW(self, ctx:coolParser.WContext):
        pass

    # Exit a parse tree produced by coolParser#w.
    def exitW(self, ctx:coolParser.WContext):
        pass


    # Enter a parse tree produced by coolParser#less_than.
    def enterLess_than(self, ctx:coolParser.Less_thanContext):
        pass

    # Exit a parse tree produced by coolParser#less_than.
    def exitLess_than(self, ctx:coolParser.Less_thanContext):
        pass


    # Enter a parse tree produced by coolParser#equals.
    def enterEquals(self, ctx:coolParser.EqualsContext):
        pass

    # Exit a parse tree produced by coolParser#equals.
    def exitEquals(self, ctx:coolParser.EqualsContext):
        pass


    # Enter a parse tree produced by coolParser#let_in.
    def enterLet_in(self, ctx:coolParser.Let_inContext):
        pass

    # Exit a parse tree produced by coolParser#let_in.
    def exitLet_in(self, ctx:coolParser.Let_inContext):
        pass


    # Enter a parse tree produced by coolParser#divide.
    def enterDivide(self, ctx:coolParser.DivideContext):
        pass

    # Exit a parse tree produced by coolParser#divide.
    def exitDivide(self, ctx:coolParser.DivideContext):
        pass


    # Enter a parse tree produced by coolParser#multiply.
    def enterMultiply(self, ctx:coolParser.MultiplyContext):
        pass

    # Exit a parse tree produced by coolParser#multiply.
    def exitMultiply(self, ctx:coolParser.MultiplyContext):
        pass


    # Enter a parse tree produced by coolParser#if_else.
    def enterIf_else(self, ctx:coolParser.If_elseContext):
        pass

    # Exit a parse tree produced by coolParser#if_else.
    def exitIf_else(self, ctx:coolParser.If_elseContext):
        pass


    # Enter a parse tree produced by coolParser#substract.
    def enterSubstract(self, ctx:coolParser.SubstractContext):
        pass

    # Exit a parse tree produced by coolParser#substract.
    def exitSubstract(self, ctx:coolParser.SubstractContext):
        pass


    # Enter a parse tree produced by coolParser#case_stat.
    def enterCase_stat(self, ctx:coolParser.Case_statContext):
        pass

    # Exit a parse tree produced by coolParser#case_stat.
    def exitCase_stat(self, ctx:coolParser.Case_statContext):
        pass


    # Enter a parse tree produced by coolParser#let_decl.
    def enterLet_decl(self, ctx:coolParser.Let_declContext):
        pass

    # Exit a parse tree produced by coolParser#let_decl.
    def exitLet_decl(self, ctx:coolParser.Let_declContext):
        pass


    # Enter a parse tree produced by coolParser#primary.
    def enterPrimary(self, ctx:coolParser.PrimaryContext):
        pass

    # Exit a parse tree produced by coolParser#primary.
    def exitPrimary(self, ctx:coolParser.PrimaryContext):
        pass



del coolParser