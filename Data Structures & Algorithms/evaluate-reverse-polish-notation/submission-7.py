class Solution:
    def __init__(self):
        self.arith = ["+", "-", "*", "/"]

    def do_operation(self, l, r, op):
        if op == "+":
            return l + r
        elif op == "-":
            return l - r
        elif op == "*":
            return l * r
        elif op == "/":
            return int(l / r)
        else:
            return -1

    
    def collapse(self, stack): # collapses (l r op) into (int) in stack
        op = stack.pop()
        r = int(stack.pop())
        l = int(stack.pop())
        res = self.do_operation(l, r, op)
        stack.append(str(res))


    def full_expression(self, stack): # checks if stack can be collapsed
        if len(stack) < 3:
            return False

        cond1 = stack[-3] not in self.arith # should be number
        cond2 = stack[-2] not in self.arith # should be number
        cond3 = stack[-1] in self.arith     # should be arith expression
        return (cond1 and cond2 and cond3)


    def evalRPN(self, tokens: List[str]) -> int:
        done = False
        stack = []
        while len(tokens) > 0:
            stack.append(tokens[0])
            tokens = tokens[1:]
            if self.full_expression(stack):
                self.collapse(stack)

        return int(stack[0])
            
        




            

        
        