class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        left, right = 0, len(s)-1
        while left < right:
            if s[left].isalpha() and s[right].isalpha():

                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left].isalpha() and not s[right].isalpha():
                right -=1
            else:
                left+=1


        return ''.join(s)