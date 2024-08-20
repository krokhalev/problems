class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        tmp = []
        for i in range(1, numRows + 1):
            row = [0] * i
            row[0] = 1
            row[-1] = 1

            if i > 2:
                for j in range(1, len(row) - 1):
                    row[j] = tmp[j - 1]

            tmp = []
            for el in range(len(row) - 1):
                tmp.append(row[el] + row[el + 1])

            res.append(row)

        return res


s = Solution()
print(s.generate(7))
