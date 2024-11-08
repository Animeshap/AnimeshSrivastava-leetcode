class Solution:
    def thousandSeparator(self, n: int) -> str:
        # Convert to string and reverse to group digits from the end
        s = str(n)[::-1]
        # Insert dots every 3 characters
        parts = [s[i:i+3] for i in range(0, len(s), 3)]
        # Join parts with dots and reverse back to original order
        return '.'.join(parts)[::-1]
