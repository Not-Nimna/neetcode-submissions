class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for val in s:
            if val in freq.keys():
                freq[val] = freq[val] + 1
            else:
                freq[val] = 1

        freq2 = {}
        for val in t:
            if val in freq2.keys():
                freq2[val] = freq2[val] + 1
            else:
                freq2[val] = 1        


        if freq == freq2:
            return True
        return False