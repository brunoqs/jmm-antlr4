# Generated from jmm.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jmmParser import jmmParser
else:
    from jmmParser import jmmParser

# This class defines a complete listener for a parse tree produced by jmmParser.
class jmmListener(ParseTreeListener):

    # Enter a parse tree produced by jmmParser#compilationUnit.
    def enterCompilationUnit(self, ctx:jmmParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by jmmParser#compilationUnit.
    def exitCompilationUnit(self, ctx:jmmParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by jmmParser#qualifiedIdentifier.
    def enterQualifiedIdentifier(self, ctx:jmmParser.QualifiedIdentifierContext):
        pass

    # Exit a parse tree produced by jmmParser#qualifiedIdentifier.
    def exitQualifiedIdentifier(self, ctx:jmmParser.QualifiedIdentifierContext):
        pass


    # Enter a parse tree produced by jmmParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:jmmParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by jmmParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:jmmParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by jmmParser#modifiers.
    def enterModifiers(self, ctx:jmmParser.ModifiersContext):
        pass

    # Exit a parse tree produced by jmmParser#modifiers.
    def exitModifiers(self, ctx:jmmParser.ModifiersContext):
        pass


    # Enter a parse tree produced by jmmParser#classDeclaration.
    def enterClassDeclaration(self, ctx:jmmParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by jmmParser#classDeclaration.
    def exitClassDeclaration(self, ctx:jmmParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by jmmParser#classBody.
    def enterClassBody(self, ctx:jmmParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by jmmParser#classBody.
    def exitClassBody(self, ctx:jmmParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by jmmParser#memberDecl.
    def enterMemberDecl(self, ctx:jmmParser.MemberDeclContext):
        pass

    # Exit a parse tree produced by jmmParser#memberDecl.
    def exitMemberDecl(self, ctx:jmmParser.MemberDeclContext):
        pass


    # Enter a parse tree produced by jmmParser#block.
    def enterBlock(self, ctx:jmmParser.BlockContext):
        pass

    # Exit a parse tree produced by jmmParser#block.
    def exitBlock(self, ctx:jmmParser.BlockContext):
        pass


    # Enter a parse tree produced by jmmParser#blockStatement.
    def enterBlockStatement(self, ctx:jmmParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by jmmParser#blockStatement.
    def exitBlockStatement(self, ctx:jmmParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by jmmParser#statement.
    def enterStatement(self, ctx:jmmParser.StatementContext):
        pass

    # Exit a parse tree produced by jmmParser#statement.
    def exitStatement(self, ctx:jmmParser.StatementContext):
        pass


    # Enter a parse tree produced by jmmParser#formalParameters.
    def enterFormalParameters(self, ctx:jmmParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by jmmParser#formalParameters.
    def exitFormalParameters(self, ctx:jmmParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by jmmParser#formalParameter.
    def enterFormalParameter(self, ctx:jmmParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by jmmParser#formalParameter.
    def exitFormalParameter(self, ctx:jmmParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by jmmParser#parExpression.
    def enterParExpression(self, ctx:jmmParser.ParExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#parExpression.
    def exitParExpression(self, ctx:jmmParser.ParExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#localVariableDeclarationStatement.
    def enterLocalVariableDeclarationStatement(self, ctx:jmmParser.LocalVariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by jmmParser#localVariableDeclarationStatement.
    def exitLocalVariableDeclarationStatement(self, ctx:jmmParser.LocalVariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by jmmParser#variableDeclarators.
    def enterVariableDeclarators(self, ctx:jmmParser.VariableDeclaratorsContext):
        pass

    # Exit a parse tree produced by jmmParser#variableDeclarators.
    def exitVariableDeclarators(self, ctx:jmmParser.VariableDeclaratorsContext):
        pass


    # Enter a parse tree produced by jmmParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:jmmParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by jmmParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:jmmParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by jmmParser#variableInitializer.
    def enterVariableInitializer(self, ctx:jmmParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by jmmParser#variableInitializer.
    def exitVariableInitializer(self, ctx:jmmParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by jmmParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:jmmParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by jmmParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:jmmParser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by jmmParser#arguments.
    def enterArguments(self, ctx:jmmParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by jmmParser#arguments.
    def exitArguments(self, ctx:jmmParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by jmmParser#tipe.
    def enterTipe(self, ctx:jmmParser.TipeContext):
        pass

    # Exit a parse tree produced by jmmParser#tipe.
    def exitTipe(self, ctx:jmmParser.TipeContext):
        pass


    # Enter a parse tree produced by jmmParser#basicType.
    def enterBasicType(self, ctx:jmmParser.BasicTypeContext):
        pass

    # Exit a parse tree produced by jmmParser#basicType.
    def exitBasicType(self, ctx:jmmParser.BasicTypeContext):
        pass


    # Enter a parse tree produced by jmmParser#referenceType.
    def enterReferenceType(self, ctx:jmmParser.ReferenceTypeContext):
        pass

    # Exit a parse tree produced by jmmParser#referenceType.
    def exitReferenceType(self, ctx:jmmParser.ReferenceTypeContext):
        pass


    # Enter a parse tree produced by jmmParser#statementExpression.
    def enterStatementExpression(self, ctx:jmmParser.StatementExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#statementExpression.
    def exitStatementExpression(self, ctx:jmmParser.StatementExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#expression.
    def enterExpression(self, ctx:jmmParser.ExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#expression.
    def exitExpression(self, ctx:jmmParser.ExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:jmmParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:jmmParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx:jmmParser.ConditionalAndExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#conditionalAndExpression.
    def exitConditionalAndExpression(self, ctx:jmmParser.ConditionalAndExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#equalityExpression.
    def enterEqualityExpression(self, ctx:jmmParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#equalityExpression.
    def exitEqualityExpression(self, ctx:jmmParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#relationalExpression.
    def enterRelationalExpression(self, ctx:jmmParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#relationalExpression.
    def exitRelationalExpression(self, ctx:jmmParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:jmmParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:jmmParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:jmmParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:jmmParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#unaryExpression.
    def enterUnaryExpression(self, ctx:jmmParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#unaryExpression.
    def exitUnaryExpression(self, ctx:jmmParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#simpleUnaryExpression.
    def enterSimpleUnaryExpression(self, ctx:jmmParser.SimpleUnaryExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#simpleUnaryExpression.
    def exitSimpleUnaryExpression(self, ctx:jmmParser.SimpleUnaryExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#postfixExpression.
    def enterPostfixExpression(self, ctx:jmmParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by jmmParser#postfixExpression.
    def exitPostfixExpression(self, ctx:jmmParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by jmmParser#selector.
    def enterSelector(self, ctx:jmmParser.SelectorContext):
        pass

    # Exit a parse tree produced by jmmParser#selector.
    def exitSelector(self, ctx:jmmParser.SelectorContext):
        pass


    # Enter a parse tree produced by jmmParser#primary.
    def enterPrimary(self, ctx:jmmParser.PrimaryContext):
        pass

    # Exit a parse tree produced by jmmParser#primary.
    def exitPrimary(self, ctx:jmmParser.PrimaryContext):
        pass


    # Enter a parse tree produced by jmmParser#creator.
    def enterCreator(self, ctx:jmmParser.CreatorContext):
        pass

    # Exit a parse tree produced by jmmParser#creator.
    def exitCreator(self, ctx:jmmParser.CreatorContext):
        pass


    # Enter a parse tree produced by jmmParser#newArrayDeclarator.
    def enterNewArrayDeclarator(self, ctx:jmmParser.NewArrayDeclaratorContext):
        pass

    # Exit a parse tree produced by jmmParser#newArrayDeclarator.
    def exitNewArrayDeclarator(self, ctx:jmmParser.NewArrayDeclaratorContext):
        pass


    # Enter a parse tree produced by jmmParser#literal.
    def enterLiteral(self, ctx:jmmParser.LiteralContext):
        pass

    # Exit a parse tree produced by jmmParser#literal.
    def exitLiteral(self, ctx:jmmParser.LiteralContext):
        pass


