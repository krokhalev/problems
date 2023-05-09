class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = []
        for t1Index in range(len(temperatures)):
            if t1Index + 1 == len(temperatures):
                res.append(0)
                break
            tmp = 1
            for t2Index in range(t1Index + 1, len(temperatures)):
                if temperatures[t1Index] < temperatures[t2Index]:
                    res.append(tmp)
                    break
                elif temperatures[t1Index] == temperatures[t2Index] and t2Index + 1 == len(temperatures):
                    res.append(0)
                    break
                else:
                    if t2Index + 1 == len(temperatures) and temperatures[t1Index] > temperatures[-1]:
                        res.append(0)
                        break
                    tmp += 1

        return res


s = Solution()
print(s.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
