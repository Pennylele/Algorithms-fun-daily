# ok an optimized way of looping through the strings once and do the comparison is to create unique keys
# Also, the tricky part to deal with the wrap-around situation is to for example, 'az' and 'ba' should map to the same "shift group" as a + 1 = b and z + 1 = a. Given the above point, the respective tuples would be (25,) (122 - 97) and (-1,) (79 - 80) and az and ba would map to different groups. This is incorrect.
# To account for this case, we add 26 to the difference between letters (smallest difference possible is -25, za) and mod by 26. So, (26 + 122 - 97) % 26 and (26 + 79 - 80) % 26 both equal (25,)
az = 97 + 122
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        MAP = collections.defaultdict(list)
        ans = []
        for string in strings:
            keys = []
            for i in range(len(string)-1):
                n = (26 + ord(string[i+1]) - ord(string[i])) % 26
                keys.append(str(n))
            final_key = ','.join(keys)
            MAP[final_key].append(string)
        ans += [MAP[k] for k in MAP]
        return ans