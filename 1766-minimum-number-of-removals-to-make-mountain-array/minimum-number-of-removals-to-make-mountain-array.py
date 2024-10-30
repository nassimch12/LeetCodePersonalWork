class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        lis = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        lds = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)

        max_mountain = 0
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                max_mountain = max(max_mountain, lis[i] + lds[i] - 1)

        return n - max_mountain if max_mountain >= 3 else -1




        