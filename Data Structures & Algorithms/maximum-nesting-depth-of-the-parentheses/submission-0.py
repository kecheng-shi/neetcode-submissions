class Solution:
    def maxDepth(self, s: str) -> int:
        curr = 0
        max_depth = 0
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
                curr += 1
                max_depth = max(max_depth, curr)
            elif char == ')':
                stack.pop()
                curr -= 1
        return max_depth