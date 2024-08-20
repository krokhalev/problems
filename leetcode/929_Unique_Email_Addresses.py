class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        res = []
        for email in emails:
            email = email.split("@")
            email[0] = email[0].replace(".", "").split("+")[0] + "@"
            email = "".join(email)
            if email not in res:
                res.append(email)

        return len(res)


s = Solution()
print(s.numUniqueEmails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
))
