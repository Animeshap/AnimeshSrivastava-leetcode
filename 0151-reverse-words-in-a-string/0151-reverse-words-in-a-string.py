class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        i=0
        j=len(s)-1
        rev=list(s)
        while i<j:
            rev[i],rev[j]=rev[j],rev[i]
            i+=1
            j-=1
        return ' '.join(rev)
