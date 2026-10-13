class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        seen = set()
        seen.add((0,0))

        for l in path:
            if l == 'N':
                y += 1
            elif l == 'S':
                y -= 1
            elif l == 'E':
                x += 1
            else:
                x -= 1
            

            if (x, y) in seen:
                return True
            seen.add((x,y))


        return False
