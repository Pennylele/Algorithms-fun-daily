# April 26, 2021
class Solution:
    def findSecretWord(self, wordlist, master):
        def findCandidate(updated_list):
            # find a candidate word in the list to call the APIs.
            alph_board = [[0] * 26 for _ in range(6)]

            # calculating the total score from all chars
            for word in wordlist:
                for i, alph in enumerate(word):
                    idx = ord(alph) - ord("a")
                    alph_board[i][idx] += 1
            # calculate the score for each word
            max_score = 0
            for word in wordlist:
                score = 0
                for alph in word:
                    idx = ord(alph) - ord("a")
                    score += alph_board[i][idx]
                if max_score < score:
                    candidate = word
                    max_score = score
            return candidate

        # compare the candidate word and each word in the list
        def pair_match(a, b):
            count = 0
            for i, j in zip(a, b):
                if i == j:
                    count += 1
            return count

        # update the list based on the API result
        updated_list = wordlist[:]
        while updated_list:
            best_word = findCandidate(updated_list)
            matches = master.guess(best_word)
            if matches == 6:
                return best_word
            else:
                updated_list = [i for i in updated_list if pair_match(i, best_word) == matches]


        