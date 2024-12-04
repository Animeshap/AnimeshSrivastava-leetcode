class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j=0
        for i in range(len(str1)):
            if j<len(str2):
                if str1[i]==str2[j]:
                    j+=1
                elif (ord(str1[i])-ord('a')+1)%26==ord(str2[j])-ord('a'):
                    j+=1
        return j==len(str2)
