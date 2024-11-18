class Solution:
    def arrangeWords(self, text: str) -> str:
        word=text.split()
        word[0]=word[0].lower()
        word.sort(key=len)
        result=' '.join(word)
        return result.capitalize()