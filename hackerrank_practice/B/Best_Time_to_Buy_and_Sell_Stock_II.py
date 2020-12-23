class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)==0):
            return 0
        hold = 0
        have = False
        earn = 0
        for i in range(len(prices)-1):
            money = prices[i + 1] - prices[i]
            if(money > 0):
                if(have==False):
                    hold = prices[i]
                    have = True
            elif(money<0):
                if(have):
                    earn += prices[i] - hold
                    have = False
        if(have):
            earn += prices[len(prices)-1] - hold
        return earn
