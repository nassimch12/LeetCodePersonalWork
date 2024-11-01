class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """

        res_list = []

        for char in s:
            if len(res_list) >= 2 and res_list[-1] == res_list[-2] == char:
                continue
            res_list.append(char)

        return "".join(res_list)
        