class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        res=list(s)
        while i<j:
            if s[i] not in 'aeiouAEIOU':
                i+=1
            elif s[j] not in 'aeiouAEIOU':
                j-=1
            else:
                res[i],res[j]=res[j],res[i]
                i+=1
                j-=1
        return ''.join(res)