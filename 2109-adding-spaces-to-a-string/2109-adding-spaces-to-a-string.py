class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        i=0
        for j in range(len(s)):
            if i<len(spaces) and spaces[i]==j :
                res.append(' ')
                i+=1
            res.append(s[j])
        return ''.join(res)
