class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def encode(s):
            res = [0] * 128
            for char in s:
                res[ord(char)-ord('a')] += 1
            return tuple(res)


        ana_map = defaultdict(list)

        for s in strs:
            ana_map[encode(s)].append(s)
        
        return [i[1] for i in ana_map.items()]

        