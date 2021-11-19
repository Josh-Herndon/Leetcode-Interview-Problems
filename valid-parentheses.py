class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2:
            return False
        
        stack = []
        closed_stack = []
        
        closed = [')', ']', '}']
        opened = ['(', '[', '{']
        complete = ['()', '[]', '{}']
        
        for ele in s:
            stack.append(ele)
        
        while stack:
            ele = stack.pop()
            if ele in closed:
                closed_stack.append(ele)
            elif ele in opened:
                if closed_stack:
                    if ele + closed_stack.pop() not in complete:
                        return False
                else:
                    return False
        
        if closed_stack or stack:
            return False
                
        return True