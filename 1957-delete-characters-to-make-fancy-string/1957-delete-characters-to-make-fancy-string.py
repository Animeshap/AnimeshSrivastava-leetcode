class Solution:
    def makeFancyString(self, s: str) -> str:
        count=1
        res=[]
        res.append(s[0])
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                count+=1
            else:
                count=1

            if count<3:
                res.append(s[i])
        return ''.join(res)