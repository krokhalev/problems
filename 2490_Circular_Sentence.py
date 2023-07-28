class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_arr = sentence.split(" ")
        tmp = sentence_arr[0][-1]
        for word in sentence_arr[1:]:
            if word[0] != tmp:
                return False
            else:
                tmp = word[-1]

        if sentence_arr[0][0] != sentence_arr[-1][-1]:
            return False

        return True


s = Solution()
print(s.isCircularSentence(sentence="leetcode exercises sound delightful"))
