class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        res = 0
        operators = ["+", "-", "*", "/"]

        index = 0
        while True:
            if index < len(tokens):
                if tokens[index] in operators:
                    if tokens[index - 2] not in operators and tokens[index - 1] not in operators:
                        if tokens[index] == "+":
                            res = int(tokens[index - 2]) + int(tokens[index - 1])
                        if tokens[index] == "-":
                            res = int(tokens[index - 2]) - int(tokens[index - 1])
                        if tokens[index] == "*":
                            res = int(tokens[index - 2]) * int(tokens[index - 1])
                        if tokens[index] == "/":
                            res = int(int(tokens[index - 2]) / int(tokens[index - 1]))

                        tokens = tokens[:index - 2] + [str(res)] + tokens[index + 1:]
                    index = 0
            else:
                break

            index += 1

        return int(tokens[-1])


s = Solution()
print(s.evalRPN(
    ["-78", "-33", "196", "+", "-19", "-", "115", "+", "-", "-99", "/", "-18", "8", "*", "-86", "-", "-", "16", "/",
     "26", "-14", "-", "-", "47", "-", "101", "-", "163", "*", "143", "-", "0", "-", "171", "+", "120", "*", "-60", "+",
     "156", "/", "173", "/", "-24", "11", "+", "21", "/", "*", "44", "*", "180", "70", "-40", "-", "*", "86", "132",
     "-84", "+", "*", "-", "38", "/", "/", "21", "28", "/", "+", "83", "/", "-31", "156", "-", "+", "28", "/", "95",
     "-", "120", "+", "8", "*", "90", "-", "-94", "*", "-73", "/", "-62", "/", "93", "*", "196", "-", "-59", "+", "187",
     "-", "143", "/", "-79", "-89", "+", "-"]))
