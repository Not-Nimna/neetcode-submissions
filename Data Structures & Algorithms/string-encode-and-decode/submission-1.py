class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for val in strs:
            res += str(len(val)) + "-" + val
        return res

    def decode(self, s: str) -> List[str]:
        ret_arr = []
        itert = 0
        while itert < len(s) :

            if s[itert].isdigit():
                wrd_len = ""
                while s[itert] != "-":
                    wrd_len += s[itert] 
                    itert += 1
                
            itert += 1
            wrd_str = ""
            for i in range(int(wrd_len)):
                wrd_str += s[itert]
                itert += 1
            ret_arr.append(wrd_str)

        return ret_arr