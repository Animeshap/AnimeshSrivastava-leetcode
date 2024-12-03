class Solution:
    def lps(self, pat):
        # Compute the longest prefix-suffix (LPS) array for the KMP algorithm
        lps = [0] * len(pat)
        length = 0
        i = 1
        while i < len(pat):
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()  # Split the sentence into words
        for index, word in enumerate(words, start=1):
            # Use KMP algorithm to check for `searchWord` as a prefix
            lps = self.lps(searchWord)
            i = 0
            j = 0
            while i < len(word):
                if word[i] == searchWord[j]:
                    i += 1
                    j += 1
                if j == len(searchWord):  # Found a match
                    if i == j:  # Match occurs at the beginning of the word
                        return index
                    j = lps[j - 1]
                elif i < len(word) and word[i] != searchWord[j]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
        return -1  # No match found
