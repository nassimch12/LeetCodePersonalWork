class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """

        counter = 1
        i = 0

        comp = []

        while i < len(word):
            while i + 1 < len(word) and word[i] == word[i + 1] and counter < 9 :
                counter += 1
                i += 1
            i += 1
            comp.append(str(counter))
            comp.append(word[i-1])

            counter = 1

        return "".join(comp)

            
        