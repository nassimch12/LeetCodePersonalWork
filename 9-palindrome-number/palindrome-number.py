class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        pal = True

        nbr = str(x)

        for i in range(len(nbr) / 2) :
            if nbr[i] != nbr[len(nbr)- i - 1]:
                pal = False
        
        return pal

        