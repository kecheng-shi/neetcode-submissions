class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bank = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill == 10:
                if bank[5] < 1:
                    return False
                bank[5] -= 1
            elif bill == 20:
                if bank[10] > 0:
                    bank[10] -= 1
                    if bank[5] > 0:
                        bank[5] -= 1
                    else:
                        return False
                elif bank [5] > 2:
                    bank[5] -= 3
                else:
                    return False
            bank[bill] += 1
            
        return True