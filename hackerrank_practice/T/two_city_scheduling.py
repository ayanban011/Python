class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        res = []
        bSum = 0
        for cost in costs:
            res.append(cost[1] - cost[0])
            bSum += cost[1]
        
        res.sort()
#         print(res)
        for index in range(len(res) // 2 , len(res)):
#             print(res[index])
            bSum -= res[index]
        
        return bSum 
