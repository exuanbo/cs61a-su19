
from typing import List, Union, Tuple, Optional
from datamodel import Pair, Expression, Nil, Number, NilType
from scheme_exceptions import OperandDeduceError, MathError, CallableResolutionError


def pair_to_list(pos: Pair) -> List[Expression]:
    out = []
    while (pos is not Nil):
        if (not isinstance(pos, Pair)):
            raise OperandDeduceError(
                ''.join(["List terminated with '", '{}'.format(pos), "', not nil"]))
        out.append(pos.first)
        pos = pos.rest
    return out


def dotted_pair_to_list(pos: Expression) -> Tuple[(List[Expression], Optional[Expression])]:
    out = []
    vararg = None
    while (pos is not Nil):
        if (not isinstance(pos, Pair)):
            vararg = pos
            break
        out.append(pos.first)
        pos = pos.rest
    return (out, vararg)


def assert_all_numbers(operands):
    for operand in operands:
        if (not isinstance(operand, Number)):
            raise MathError(''.join(
                ['Unable to perform arithmetic, as ', '{}'.format(operand), ' is not a number.']))


def verify_exact_callable_length(operator: Expression, expected: int, actual: int):
    if (expected != actual):
        raise CallableResolutionError(''.join(['{}'.format(operator), ' expected ', '{}'.format(
            expected), ' operands, received ', '{}'.format(actual), '.']))


def verify_min_callable_length(operator: Expression, expected: int, actual: int):
    if (expected > actual):
        raise CallableResolutionError(''.join(['{}'.format(operator), ' expected at least ', '{}'.format(
            expected), ' operands, received ', '{}'.format(actual), '.']))


def make_list(exprs: List[Expression], last: Expression = Nil) -> Union[(Pair, NilType)]:
    out = last
    for expr in reversed(exprs):
        out = Pair(expr, out)
    return out
