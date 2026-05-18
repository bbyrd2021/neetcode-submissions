class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #booleana array
        s_bool = [0] * 128
        t_bool = [0] * 128

        for char in s:
            s_bool[ord(char)] += 1
        for char in t:
            t_bool[ord(char)] += 1

        if s_bool == t_bool: return True


        return False
        