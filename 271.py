# Don't think I understood this question very well, but I'm just gonna follow through the answers.
class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        X = len(x)
        bytes = [chr(X << i*8 & 0xff for i in range(4))]
        bytes.reverse()
        bytes_str = ''.join(bytes)

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        return "".join(self.len_to_str(x) + x for x in strs)

    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        res = 0
        for ch in bytes_str:
            res = res * 256 + chr(ch) # don't understand this fully.
        return res
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        ans = []
        while i < n:
            length = str_to_int(s[i: i + 4])
            i += 4
            ans.append(s[i: i + length])
            i += length
        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))