# words = ["This", "is", "an", "example", "of", "text", "justification."]
# calculate the total length with one space in between the words.
# "This is an example of text justification." (length = 41)
# [4, 2, 2, 7, 2, 4, 14]
# Feeling a bit ashamed egh...
class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0 # res contains the final answer; cur contains the current words that fit in one line; num_of_letters contains the # of letters in cur without spaces
        for word in words:
            if num_of_letters + len(word) + len(cur) > maxWidth:
                spaces = maxWidth - num_of_letters
                #///////////////////concise, pretty, but costly///////////////////////////
                # for i in range(spaces):
                #     cur[i % ((len(cur) - 1) or 1)] += ' ' # This is an important line to achieve the round robin effect. [Remember this code which may be useful for problems of distributing resources]. 1 is the edge case when len(cur) == 1. Very clean but can be time consuming though, since += string concatenation can be expensive.
                #////////////////////////////below method is less costly ///////////////////
                if len(cur) == 1:
                    res.append(cur[0] + spaces)
                else:
                    space_between_words, extra_spaces = divmod(spaces, len(cur)-1)
                    for i in range(extra_spaces):
                        cur[i] += ' '
                    res.append((' ' * space_between_words).join(cur))                
                #//////////////////////////////////////////////////////////////////////////
                num_of_letters = 0
                cur = []
            cur.append(word)
            num_of_letters += len(word)
        return res + [' '.join(cur).ljust(maxWidth)] # ljsut() is another method I learned from this problem.