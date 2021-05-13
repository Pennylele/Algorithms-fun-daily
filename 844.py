# "a#c###"
# "ad#c"
class Solution:
    def backspaceCompare(self, S, T):
        s, t = len(S)-1, len(T)-1
        backspace_s = backspace_t = 0

        while s >= 0 or t >= 0:
            
            while s >= 0:
                if S[s] == "#":
                    backspace_s += 1
                    s -= 1
                elif S[s] != "#" and backspace_s > 0:
                    backspace_s -= 1
                    s -= 1
                elif S[s] != "#" and backspace_s == 0:
                    break
            

            while t >= 0:
                if T[t] == "#":
                    backspace_t += 1
                    t -= 1
                elif T[t] != "#" and backspace_t > 0:
                    t -= 1
                    backspace_t -= 1
                elif T[t] != "#" and backspace_t == 0:
                    break 
            
            if (s < 0 and t >= 0) or (t < 0 and s >= 0):
                return False
            if s >= 0 and t >= 0 and S[s] != T[t]:
                return False
            s -= 1
            t -= 1
            print(s, t)
        
        return True