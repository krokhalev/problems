class Solution:
    def groupAnagrams(self, strs: list[str]):
        map = {}
        for an in strs:
            if "".join(sorted(an)) in map:
                map["".join(sorted(an))].append(an)
            else:
                map["".join(sorted(an))] = [an]

        return map.values()


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

