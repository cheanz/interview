
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
            
        
        sumofsubstrings=0
        startindex=0

        while startindex < reallength:
            n=0
            m=0
            while m < maxlengthofsub and n < maxlengthofsub :
                    if startindex+m >= reallength:
                        break
                    if  s[startindex+m] == t[n]:
                        m += 1                    
                    n += 1
            sumofsubstrings += 1
            startindex = startindex + m
            # print('m:')
            # print(m)
            # print(startindex)
        return sumofsubstrings

print(Solution.lengthOfLongestSubstring(Solution,'abc','a'))
