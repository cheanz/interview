
class Solution:
    def lengthOfLongestSubstring(self, t: str, s: str) -> int:
        '''
        t="abc"
        s="abcbc"
        '''
        maxlengthofsub=len(t)
        reallength=len(s)
        for i in s:
            if i not in t:
                return -1
            
        m=0
        sumofsubstrings=0
        startindex=0

        while startindex < reallength:
            n=0
            while m < maxlengthofsub and n < maxlengthofsub :
                    if startindex+m >= reallength:
                        break
                    if  s[startindex+m] == t[n]:
                        m += 1
                    else:
                        n += 1
            sumofsubstrings += 1
            startindex = startindex + m - 1
        return sumofsubstrings

print(Solution.lengthOfLongestSubstring(Solution,'xyz','z'))
