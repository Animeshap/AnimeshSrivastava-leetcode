class Solution:
    def minChanges(self, s: str) -> int:
        total=0
        for i in range(1,len(s),2):
            if s[i-1]!=s[i]:
                total+=1
        return total

