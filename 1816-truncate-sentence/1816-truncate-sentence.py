class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()  # Split the sentence into a list of words
        truncated_words = []  # List to store the first k words
        
        for i in range(k):
            truncated_words.append(words[i])  # Append the first k words to the list
        
        return ' '.join(truncated_words)  # Join the words back into a string
