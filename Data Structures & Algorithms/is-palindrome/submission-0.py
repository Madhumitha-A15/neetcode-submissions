class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) -1

        while(first < last):
            
            if not (s[first].lower().isalnum()):
                first+=1
            elif  not (s[last].lower().isalnum()) :
                last-=1
            else:
                if (s[first].lower() != s[last].lower()):
                    return False
                else:
                    first+=1
                    last-=1

        return True