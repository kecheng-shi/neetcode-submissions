class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        x, y = 0, 0
        seen.add((0, 0))

        for c in path:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            else:
                x -= 1

            if (x, y) in seen:
                return True
            
            seen.add((x, y))

        return False