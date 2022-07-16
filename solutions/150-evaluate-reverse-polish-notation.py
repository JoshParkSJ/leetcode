# O(n) time | O(1) space
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for symbol in tokens:
            if symbol in "+-*/":
                firstNum = numbers.pop()
                secondNum = numbers.pop()
                numbers.append(self.calculate(firstNum, symbol, secondNum))
            else:
                numbers.append(int(symbol))
        return numbers[-1]
            
    def calculate(self, firstNum, symbol, secondNum):
        if symbol == "+":
            return firstNum + secondNum
        if symbol == "-":
            return secondNum - firstNum # order has to be reversed (3-4) vs (4-3)
        if symbol == "*": 
            return firstNum * secondNum
        if symbol == "/":
            return int(secondNum / firstNum) # order has to be reversed (2/4) vs (4/2)