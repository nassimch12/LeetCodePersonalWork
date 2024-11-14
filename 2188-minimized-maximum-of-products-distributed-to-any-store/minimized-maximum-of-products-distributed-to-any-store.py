class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """

        def canDistribute(k):
            stores = 0
            for i in quantities:
                stores += (i + k - 1) // k

            return stores <= n

        left,right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1
                
        return left

                

        