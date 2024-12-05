class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if len(start)!=len(target):
            return False
        i=0
        j=0
        n=len(start)
        blank='_'
        left='L'
        right='R'
        while i<n or j<n:
            while  i<n and start[i]==blank:
                i+=1
            while j<n and target[j]==blank:
                j+=1
            if i==n or j==n:
                break
            if start[i]!=target[j]:
                return False
            if start[i]==left and i<j:
                return False
            if start[i]==right and i>j:
                return False
            i+=1
            j+=1
        return i==n and j==n  

