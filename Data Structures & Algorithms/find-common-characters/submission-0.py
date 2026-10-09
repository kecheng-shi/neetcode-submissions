class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        dic_list = []
        for i in range(n):
            dic = {}
            for char in words[i]:
                if char in dic:
                    dic[char] += 1
                else:
                    dic[char] = 1
            dic_list.append(dic)

        res = []
        for char in dic_list[0]:
            res.extend([char] * min(d.get(char, 0) for d in dic_list))
            
        return res