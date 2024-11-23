class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn=False
        delta=10
        while delta <=n:
            n-=delta
            delta-=1
            turn =not turn
        return turn