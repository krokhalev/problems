class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        words = []
        word = ""
        text_len = len(text)

        for i, t in enumerate(text):
            if t == " ":
                spaces += 1
                if word != "":
                    words.append(word)
                    word = ""
            else:
                word += t

            if i == text_len - 1:
                if word != "":
                    words.append(word)
                    word = ""

        if spaces == 0:
            return text

        div_by = (len(words) - 1)
        if div_by > 0:
            division = spaces // div_by
            division_module = spaces % div_by
        else:
            return words[0] + (" " * spaces)

        inner_spaces = " " * division
        outher_spaces = " " * division_module
        res = ""
        len_words = len(words)
        if division_module > 0:
            for i, w in enumerate(words):
                if i == len_words - 1:
                    res += w + outher_spaces
                    break
                res += w + inner_spaces
        else:
            for i, w in enumerate(words):
                if i == len_words - 1:
                    res += w
                    break
                res += w + inner_spaces

        return res


s = Solution()
print(s.reorderSpaces("  hello"))
