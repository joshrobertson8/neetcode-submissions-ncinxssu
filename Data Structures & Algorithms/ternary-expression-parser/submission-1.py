class Solution:
    def parseTernary(self, expression: str) -> str:
        
        i = 0

        while True:
            cur = expression[i]

            if cur == 'T' and i < len(expression) - 1 and expression[i + 1] == "?":
                i += 2

            elif cur == 'F' and i < len(expression) - 1 and expression[i + 1] == "?":

                i += 2

                count = 1
                while count != 0 and i < len(expression) - 1:

                    if expression[i] == "?":
                        count += 1

                    elif expression[i] == ":":
                        count -= 1

                    i += 1

            else:
                break
            
        return expression[i]
    