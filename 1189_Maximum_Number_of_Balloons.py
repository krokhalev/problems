class Solution(object):
    def maxNumberOfBalloons(self, text: str):
        count = 0
        balloon = "balloon"
        while True:

            for letter in balloon:
                if letter in text:
                    text = text.replace(letter, "", 1)
                else:
                    return count
            count += 1


s = Solution()
print(s.maxNumberOfBalloons("loonbalxballpoon"))
