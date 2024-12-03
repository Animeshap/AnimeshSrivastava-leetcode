class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        m = len(pref)
        cnt = 0
        for word in words:
            if word[:m] == pref: cnt += 1
        return cnt