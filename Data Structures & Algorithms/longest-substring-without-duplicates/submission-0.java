class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int maxLen = 0;
        
        HashMap<Character, Integer> dict = new HashMap<>();
        for(int right = 0 ; right < s.length() ; right++){
            char ch = s.charAt(right);
            dict.put(ch , dict.getOrDefault(ch ,0) + 1);
            while (dict.get(ch) > 1) {
                char leftChar = s.charAt(left);          // the char leaving the window
                dict.put(leftChar, dict.get(leftChar) - 1);  // decrement the LEFT char
                left++;
        }
        maxLen = Math.max(maxLen, right - left + 1); 
        }
        return maxLen;
    
    }
}
