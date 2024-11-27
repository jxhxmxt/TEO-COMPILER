from enum import Enum

class NonTerminals(Enum):
    TRANSLATION_UNIT = 'translation_unit'
    POSTFIX_EXPRESSION = 'postfix_expression'
    ARGUMENT_EXPRESSION_LIST = 'argument_expression_list'
    UNARY_EXPRESSION = 'unary_expression'
    UNARY_OPERATOR = 'unary_operator'
    ASSIGNMENT_EXPRESSION = 'assignment_expression'
    ASSIGNMENT_OPERATOR = 'assignment_operator'
    EXPRESSION = 'expression'
    CONSTANT_EXPRESSION = 'constant_expression'
    DECLARATION = 'declaration'
    DECLARATION_V2 = 'declarationv2'
    DECLARATION_SPECIFIERS = 'declaration_specifiers'
    INIT_DECLARATOR_LIST = 'init_declarator_list'
    INIT_DECLARATOR = 'init_declarator'
    TYPE_SPECIFIER = 'type_specifier'
    STRUCT_OR_UNION_SPECIFIER = 'struct_or_union_specifier'
    STRUCT_OR_UNION = 'struct_or_union'
    STRUCT_DECLARATION_LIST = 'struct_declaration_list'
    STRUCT_DECLARATION = 'struct_declaration'
    SPECIFIER_QUALIFIER_LIST = 'specifier_qualifier_list'
    STRUCT_DECLARATOR_LIST = 'struct_declarator_list'
    STRUCT_DECLARATOR = 'struct_declarator'
    TYPE_QUALIFIER = 'type_qualifier'
    DECLARATOR = 'declarator'
    DIRECT_DECLARATOR = 'direct_declarator'
    TYPE_QUALIFIER_LIST = 'type_qualifier_list'
    IDENTIFIER_LIST = 'identifier_list'
    TYPE_NAME = 'type_name'
    INITIALIZER = 'initializer'
    INITIALIZER_LIST = 'initializer_list'
    STATEMENT = 'statement'
    LABELED_STATEMENT = 'labeled_statement'
    COMPOUND_STATEMENT = 'compound_statement'
    DECLARATION_LIST = 'declaration_list'
    STATEMENT_LIST = 'statement_list'
    EXPRESSION_STATEMENT = 'expression_statement'
    SELECTION_STATEMENT = 'selection_statement'
    ITERATION_STATEMENT = 'iteration_statement'
    EXTERNAL_DECLARATION = 'external_declaration'
    FUNCTION_DEFINITION = 'function_definition'
    BLOCK_ITEM_LIST = 'block_item_list'
    BLOCK_ITEM = 'block_item'
    PRIMARY_EXPRESSION = 'primary_expression'