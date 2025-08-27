import operator
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for t in tokens:
            if not i in operator_map:
                stack.append(int(t))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                operator_func = operator_map[t]
                stack.append(math.trunc(operator_func(first_operand, second_operand)))


        return stack.pop()
