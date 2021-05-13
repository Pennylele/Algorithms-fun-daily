def strongPasswordChecker(self, s: str) -> int:
    '''
    @lru_cache(None)
    def dp(index, numOfCh, hasLower, hasUpper, hasDigit, lastChr, secondLastChr):
        if numOfCh > 20:
            return sys.maxsize
        if index == n:
            if numOfCh >= 6 and hasLower and hasUpper and hasDigit:
                return 0
            else:
                return sys.maxsize
        ans = sys.maxsize
        c = s[index]
        # keep
        if c != lastChr or c != secondLastChr:
            ans = min(ans, dp(index + 1, numOfCh + 1,
                              hasLower or c.islower(),
                              hasUpper or c.isupper(),
                              hasDigit or c.isdigit(),
                              c,
                              lastChr))
        # insert lower case
        ans = min(ans, dp(index, numOfCh + 1,
                          True,
                          hasUpper,
                          hasDigit,
                          'y' if lastChr == 'z' else 'z',
                          lastChr) + 1)
        # insert upper case
        ans = min(ans, dp(index, numOfCh + 1,
                          hasLower,
                          True,
                          hasDigit,
                          'Y' if lastChr == 'Z' else 'Z',
                          lastChr) + 1)
        # insert digit
        ans = min(ans, dp(index, numOfCh + 1,
                          hasLower,
                          hasUpper,
                          True,
                          '8' if lastChr == '9' else '8',
                          lastChr) + 1)
        # delete
        ans = min(ans, dp(index + 1, numOfCh,
                          hasLower,
                          hasUpper,
                          hasDigit,
                          lastChr,
                          secondLastChr) + 1)
        # change to lower case
        ans = min(ans, dp(index + 1, numOfCh + 1,
                          True,
                          hasUpper,
                          hasDigit,
                          'y' if lastChr == 'z' else 'z',
                          lastChr) + 1)
        # change to upper case
        ans = min(ans, dp(index + 1, numOfCh + 1,
                          hasLower,
                          True,
                          hasDigit,
                          'Y' if lastChr == 'Z' else 'Z',
                          lastChr) + 1)
        # change to digit
        ans = min(ans, dp(index + 1, numOfCh + 1,
                          hasLower,
                          hasUpper,
                          True,
                          '8' if lastChr == '9' else '8',
                          lastChr) + 1)
        return ans
    n = len(s)
    if n == 0:
        return 6
    return dp(0,0,False,False,False,'','')
    '''

    n = len(s)

    missing_types = 3

    if any(c.islower() for c in s):
        missing_types -= 1

    if any(c.isupper() for c in s):
        missing_types -= 1

    if any(c.isdigit() for c in s):
        missing_types -= 1

    change = 0
    remove_one = 0
    remove_two = 0

    i = 2

    while i < n:
        if s[i] == s[i-1] == s[i-2]:
            length = 2
            while i < n and s[i] == s[i-1]:
                length += 1
                i += 1

            change += length // 3 # aaaaaaa

            if length % 3 == 0:
                remove_one += 1
            elif length % 3 == 1:
                remove_two += 1
        else:
            i += 1

    if n < 6:
        return max(missing_types, 6 - n)
    elif n <= 20:
        return max(missing_types, change)
    else:
        deletes = n - 20

        change -= min(deletes, remove_one)
        change -= min(max(deletes - remove_one, 0), remove_two * 2) // 2
        change -= max(deletes - remove_one - remove_two * 2, 0) // 3 

        return deletes + max(missing_types, change)