class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        
        def gesort(item):
            return ''.join(sorted(item))

        strs.sort(key=gesort)
        res.append([strs.pop(0)])
        

        while strs:
            if sorted(strs[0]) == sorted(res[-1][0]):
                res[-1].append(strs.pop(0))
            else:
                res.append([strs.pop(0)])
        
        return res
        