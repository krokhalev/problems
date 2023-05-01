class Solution:
    def average(self, salary):
        salary.sort()
        return sum(salary[1:-1])/len(salary[1:-1])


salary = [4000, 3000, 2000]
s = Solution()
print(s.average(salary))
