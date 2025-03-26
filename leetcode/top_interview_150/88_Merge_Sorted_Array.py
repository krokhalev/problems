class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if len(nums1) == 0:
            nums1.append(0)
        if len(nums2) == 0:
            nums2.append(0)
        res = []
        i = 0
        j = 0
        while True:
            if len(res) == m+n:
                return res
            n1 = nums1[i]
            n2 = nums2[j]
            if n1 == 0 and n2 != 0:
                res.append(n2)
                j += 1
                continue
            if n1 != 0 and n2 == 0:
                res.append(n1)
                i += 1
                continue
            if n1 < n2:
                res.append(n1)
                i += 1
                continue
            if n1 > n2:
                res.append(n2)
                j += 1
                continue
            if n1 == n2:
                res.append(n2)
                j += 1
                continue

        return res


s = Solution()
print(s.merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3))
