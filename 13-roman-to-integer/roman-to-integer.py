class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        ref = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        

        i = 0

        while i < len(s):
            if i + 1 < len(s):
                current_char = s[i]
                next_char = s[i+1]
            
                if current_char == 'I' and next_char == 'V':
                    val += 4
                    i += 2
                elif current_char == 'I' and next_char == 'X':
                    val += 9
                    i += 2
                elif current_char == 'X' and next_char == 'L':
                    val += 40
                    i += 2
                elif current_char == 'X' and next_char == 'C':
                    val += 90
                    i += 2
                elif current_char == 'C' and next_char == 'D':
                    val += 400
                    i += 2
                elif current_char == 'C' and next_char == 'M':
                    val += 900
                    i += 2
                else:
                    # print("[1]")
                    # print("Adding",ref[s[i]])
                    val += ref[s[i]]
                    # print("new value ", val)
                    i += 1
                    
            
            else:
                # print("[2]")
                # print("Adding", ref[s[i]])
                val += ref[s[i]]
                # print("new value", val)
                i += 1
                

        return val


        