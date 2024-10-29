class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            # Rotate s by moving the first character to the end
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False
