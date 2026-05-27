class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+" : lambda a, b : a + b,
            "-" : lambda a, b : b - a,
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : int(b/a)
        }
        for token in tokens:
            if token in operations:
                stack.append(operations[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        return stack.pop()
            
