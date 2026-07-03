class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        countS = {}
        countT = {}

        for charS in s:
            countS[charS] = countS.get(charS , 0) + 1

        for charT in t:
            countT[charT] = countT.get(charT , 0) + 1

        return countS == countT
