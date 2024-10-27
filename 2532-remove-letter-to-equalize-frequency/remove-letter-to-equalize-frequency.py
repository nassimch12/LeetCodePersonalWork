class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """

        freq = {}

        for letter in word:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1

        freq_values = list(freq.values())

        freq_count = {}
        for value in freq_values:
            if value in freq_count:
                freq_count[value] += 1
            else:
                freq_count[value] = 1

        if len(freq) == 1:
            return True

        if len(freq_count) == 1:
            return next(iter(freq_count)) == 1

        if len(freq_count) == 2:
            f1,f2 = list(freq_count.keys())
            c1,c2 = freq_count[f1], freq_count[f2]

            if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
                return True

            if abs(f1 - f2) == 1:
                if (c1 == 1 and f1 > f2) or (c2 == 1 and f2 > f1):
                    return True

        return False


        