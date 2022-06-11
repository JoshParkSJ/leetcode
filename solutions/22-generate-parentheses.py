# O(2^n) time | O(n) space
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openBrackets = 1
        numOfBrackets = 0
        result = []
        
        def createParenthesis(bracket, openBrackets, numOfBrackets):
            if numOfBrackets == n:
                result.append(bracket)
                return
            
            if openBrackets < n:
                createParenthesis(bracket+"(", openBrackets+1, numOfBrackets)

            if openBrackets > numOfBrackets:
                createParenthesis(bracket+")", openBrackets, numOfBrackets+1)
        
        createParenthesis("(", openBrackets, numOfBrackets)
        return result

## -----------------------------------------------------------------------------------

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        
        def helper(ans,open,close):
            if close == n:
                res.add(ans)
                return
                
            if open < n:
                helper(ans+"(",open+1,close)
            
            if close < open:
                helper(ans+")",open,close+1)
            
        helper("",0,0)
        return res
