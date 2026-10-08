class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr = 0
        stack = []
        for char in s:
            if char == '(':
                curr += 1
                max_depth = max(max_depth, curr)
                stack.append(char)
            elif char == ')':
                curr -= 1
                stack.pop()
        
        return max_depth