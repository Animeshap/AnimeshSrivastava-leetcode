class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        start=int(loginTime[:2])*60+int(loginTime[-2:])
        end=int(logoutTime[:2])*60+int(logoutTime[-2:])
        if start>end:
            end+=24*60
        start,end=start//15+int(start%15>0),end//15
        return max(0,end-start)