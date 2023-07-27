class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        def to_int(string):
            return int(string.replace(":", ""))

        if to_int(event1[0]) <= to_int(event2[0]) <= to_int(event1[1]):
            return True
        if to_int(event2[0]) <= to_int(event1[0]) <= to_int(event2[1]):
            return True

        return False


s = Solution()
print(s.haveConflict(event1=["01:15", "02:00"], event2=["02:00", "03:00"]))
