# Input: sentence = ["hello","world"], rows = 2, cols = 8
# Output: 1
# Explanation:
# hello---
# world---
# The character '-' signifies an empty space on the screen.
# string = "hello world "; len(string) = 12
class Solution:
    def wordsTyping(self, sentence, rows, cols):
        new_string = " ".join(sentence) + " "
        L = len(new_string)

        start = 0
        for i in range(rows):
            start += cols # 8, 14
            while new_string[start % L] != " ":
                start -= 1 # 5, 11 - start is the index where the element is a space
            start += 1 # 6, 12
        return start // L



