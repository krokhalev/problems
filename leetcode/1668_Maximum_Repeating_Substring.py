class Solution(object):
    def maxRepeating(self, sequence, word):
        len_word = len(word)
        i = 0
        tmp_i = 0
        saved_i = False
        res = 0
        tmp_res = 0
        default_step = True
        while True:
            if len_word + i >= len(sequence)+1:
                if tmp_res > res:
                    res = tmp_res
                break

            if sequence[i:i + len_word] == word:
                tmp_res += 1
                if not saved_i:
                    tmp_i = i
                    saved_i = True
                default_step = False
            else:
                default_step = True
                saved_i = False
                if tmp_i > 0:
                    i = tmp_i
                if tmp_res > res:
                    res = tmp_res

            if default_step:
                i += 1
            else:
                i += len_word

        return res


s = Solution()
print(s.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))
