from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        temp = defaultdict(list)
        for ele in strs:
            temp[str(sorted(ele))].append(ele)
        res = list(temp.values())
        return res
        
