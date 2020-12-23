def newString(S):
    q = []
    for i in range(0, len(S)):
        if(S[i] != '#'):  
            q.append(S[i])  
        elif len(q) > 0:  
            q.pop()  
  
    # Build final string  
    ans = ""
    while len(q) != 0:  
        ans += q[0]  
        q.pop(0)  
    # return final string  
    return ans
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S = newString(S)
        T = newString(T)
        if(S==T):
            return True
        else:
            return False
            
