class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k - 1
        self.nums = nums

    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]


kth = KthLargest(3, [4, 5, 8, 2])
print(kth.add(3))
