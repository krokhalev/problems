class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        for index in range(len(strs)):
            strs[index] = "*&" + strs[index] + "&*"

        return "".join(strs)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        res = str.split("&**&")
        res[0] = res[0].replace("*&", "")
        res[-1] = res[-1].replace("&*", "")
        return res


s = Solution()
encoded = s.encode(["lint", "code", "love", "you"])
print(s.decode(encoded))
