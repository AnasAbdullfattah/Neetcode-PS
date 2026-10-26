class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # the sorting solution
        # sorted_string = ''.join(sorted(s))
        # sorted_string2 = ''.join(sorted(t))

        # for i in range (len(s)):
        #     if sorted_string[i] != sorted_string2[i]:
        #         return False
        # return True

        # short sorted

        # return sorted(s) == sorted(t)

        # hashmap
        s_d = {}
        t_d = {}

        for n in s:
            if n in s_d:
                s_d[n] = s_d[n]+1
            else:
                s_d[n] = 1

                
        for n in t:
            if n in t_d:
                t_d[n] = t_d[n]+1
            else:
                t_d[n] = 1

        return s_d == t_d


        # short Dicitonary
        # s_d , t_d = {},{}
        # for i in range(len(s)):
        #     s_d[s[i]] = 1 + s_d.get(s[i],0)
        #     t_d[t[i]] = 1 + t_d.get(t[i],0)

        # return s_d == t_d

