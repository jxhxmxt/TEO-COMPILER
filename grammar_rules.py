import non_terminals as nonTerminals
import terminals as t

terminals = t.Terminals
nt = nonTerminals.NonTerminals

derivations = [
 [nt.PROGRAM.value, terminals.INT.value, [nt.FUNCTION.value]],
 [nt.PROGRAM.value, terminals.CHAR.value, [nt.FUNCTION.value]],
 [nt.PROGRAM.value, terminals.FLOAT.value, [nt.FUNCTION.value]],
 [nt.PROGRAM.value, terminals.VOID.value, [nt.FUNCTION.value]],
 [nt.PROGRAM.value, terminals.INT.value, [nt.DECLARATION.value]],
 [nt.PROGRAM.value, terminals.CHAR.value, [nt.DECLARATION.value]],
 [nt.PROGRAM.value, terminals.FLOAT.value, [nt.DECLARATION.value]],
 [nt.PROGRAM.value, terminals.LINE_COMMENT.value, [nt.COMMENT.value]],
 [nt.PROGRAM.value, terminals.COMMENT_BLOCK_START.value, [nt.COMMENT.value]],
 [nt.PROGRAM.value, terminals.INCLUDE.value, [nt.MACRO.value, nt.PROGRAM.value]],
 [nt.PROGRAM.value, terminals.DEFINE.value, [nt.MACRO.value, nt.PROGRAM.value]],
 [nt.PROGRAM.value, None, []],
 [nt.FUNCTION.value, terminals.INT.value, [terminals.IDENTIFIER.value, nt.FUNC_BODY.value]],
 [nt.FUNCTION.value, terminals.FLOAT.value, [terminals.IDENTIFIER.value, nt.FUNC_BODY.value]],
 [nt.FUNCTION.value, terminals.CHAR.value, [terminals.IDENTIFIER.value, nt.FUNC_BODY.value]],
 [nt.FUNCTION.value, terminals.VOID.value, [terminals.IDENTIFIER.value, nt.FUNC_BODY.value]],
 [nt.FUNC_BODY.value, terminals.LEFT_PAREN.value, [terminals.RIGHT_PAREN.value, terminals.LEFT_CURLY.value , nt.STATEMENT.value, terminals.RIGHT_CURLY.value]],
 [nt.DECLARATION.value, terminals.INT.value, [terminals.IDENTIFIER.value, nt.DECLARATION_BODY.value]],
 [nt.DECLARATION.value, terminals.CHAR.value, [terminals.IDENTIFIER.value, nt.DECLARATION_BODY.value]],
 [nt.DECLARATION.value, terminals.FLOAT.value, [terminals.IDENTIFIER.value, nt.DECLARATION_BODY.value]],
 [nt.DECLARATION_BODY.value, terminals.SEMICOLON.value, []],
 [nt.DECLARATION_BODY.value, terminals.EQUALS.value, [nt.EXPRESSION.value, terminals.SEMICOLON.value]],
 [nt.STATEMENT.value,  terminals.NUMBER.value, [terminals.SEMICOLON.value, nt.STATEMENT.value]],
 [nt.STATEMENT.value, terminals.IF.value, [nt.CONDITIONAL.value, nt.STATEMENT.value]],
 [nt.STATEMENT.value, terminals.LEFT_CURLY.value, [nt.STATEMENT.value, terminals.RIGHT_CURLY.value]],
 [nt.STATEMENT.value, terminals.WHILE.value, [nt.WHILE_STATEMENT.value, nt.STATEMENT.value]],
 [nt.STATEMENT.value, terminals.INT.value, [nt.DECLARATION.value, nt.STATEMENT.value]],
 [nt.STATEMENT.value, terminals.CHAR.value, [nt.DECLARATION.value, nt.STATEMENT.value]],
 [nt.STATEMENT.value, terminals.FLOAT.value, [nt.DECLARATION.value, nt.STATEMENT.value]],
 [nt.STATEMENT.value, terminals.ELSE.value, []],
 [nt.STATEMENT.value, terminals.RIGHT_CURLY.value, []],
 [nt.STATEMENT.value, terminals.LINE_COMMENT.value, []],
 [nt.STATEMENT.value, terminals.RETURN.value, [terminals.SEMICOLON.value]],
 [nt.STATEMENT.value, terminals.COMMENT_BLOCK_START.value, [terminals.COMMENT_BLOCK_END.value]],
 [nt.EXPRESSION.value, terminals.IDENTIFIER.value, [nt.EXPRESSION_ALT.value]],
 [nt.EXPRESSION.value, terminals.NUMBER.value, [nt.EXPRESSION_ALT.value]],
 [nt.EXPRESSION.value, terminals.CHARACTER.value, [nt.EXPRESSION_ALT.value]],
 [nt.EXPRESSION.value, terminals.EQUALS.value, []],
 [nt.EXPRESSION_ALT.value, terminals.IDENTIFIER.value, []],
 [nt.EXPRESSION_ALT.value, terminals.RIGHT_PAREN.value, []],
 [nt.EXPRESSION_ALT.value, terminals.ADD_OPERATOR.value, [nt.TERM.value, nt.EXPRESSION_ALT.value]],
 [nt.EXPRESSION_ALT.value, terminals.MUL_OPERATOR.value, [nt.TERM.value, nt.EXPRESSION_ALT.value]],
 [nt.EXPRESSION_ALT.value, terminals.DIV_OPERATOR.value, [nt.TERM.value, nt.EXPRESSION_ALT.value]],
 [nt.EXPRESSION_ALT.value, terminals.SUB_OPERATOR.value, [nt.TERM.value, nt.EXPRESSION_ALT.value]],
 [nt.EXPRESSION_ALT.value, None, []],
 [nt.EXPRESSION_ALT.value, terminals.NUMBER.value, []],
 [nt.EXPRESSION_ALT.value, terminals.CHARACTER.value, []],
 [nt.EXPRESSION_ALT.value, terminals.CHAR.value, []],
 [nt.EXPRESSION_ALT.value, terminals.LEFT_CURLY.value, []],
 [nt.EXPRESSION_ALT.value, terminals.SEMICOLON.value, []],
 [nt.TERM.value, terminals.IDENTIFIER.value, []],
 [nt.TERM.value, terminals.NUMBER.value, []],
 [nt.TERM.value, terminals.ADD_OPERATOR.value, []],
 [nt.TERM.value, terminals.MUL_OPERATOR.value, []],
 [nt.TERM.value, terminals.SUB_OPERATOR.value, []],
 [nt.TERM.value, terminals.DIV_OPERATOR.value, []],
 [nt.FACTOR.value, terminals.IDENTIFIER.value, []],
 [nt.FACTOR.value, terminals.NUMBER.value , []],
 [nt.CONDITIONAL.value, terminals.IF.value, [terminals.LEFT_PAREN.value, nt.EXPRESSION.value, terminals.RIGHT_PAREN.value, terminals.LEFT_CURLY.value, nt.STATEMENT.value, terminals.RIGHT_CURLY.value ,nt.CONDITIONAL_ALT.value]],
 [nt.CONDITIONAL_ALT.value, terminals.ELSE.value, [nt.STATEMENT.value]],
 [nt.CONDITIONAL_ALT.value, terminals.RIGHT_CURLY.value, []],
 [nt.CONDITIONAL_ALT.value, None, []],
 [nt.CONDITIONAL_ALT.value, terminals.LINE_COMMENT.value, []],
 [nt.ASSIGNMENT.value, terminals.IDENTIFIER.value, [terminals.EQUALS.value, nt.EXPRESSION.value]],
 [nt.DATA_TYPE.value, terminals.INT.value, None],
 [nt.DATA_TYPE.value, terminals.CHAR.value, []],
 [nt.DATA_TYPE.value, terminals.FLOAT.value, []],
 [nt.COMMENT.value, terminals.LINE_COMMENT.value, [terminals.STRING.value]],
 [nt.COMMENT.value, terminals.COMMENT_BLOCK_START.value, [terminals.STRING.value, terminals.COMMENT_BLOCK_END.value]],
 [nt.MACRO.value, terminals.INCLUDE.value, [terminals.STRING.value]],
 [nt.MACRO.value, terminals.DEFINE.value, [terminals.IDENTIFIER.value, terminals.CHARACTER.value]],
 [nt.WHILE_STATEMENT.value, terminals.WHILE.value, [terminals.LEFT_PAREN.value, nt.EXPRESSION.value, terminals.RIGHT_PAREN.value, terminals.LEFT_CURLY.value  , nt.STATEMENT.value, terminals.RIGHT_CURLY.value]]
 ]