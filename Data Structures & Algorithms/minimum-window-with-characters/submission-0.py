class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is longer than s, no valid window
        if len(t) > len(s):
            return ""
        
        # Build frequency map for t manually
        target = {}
        for c in t:
            target[c] = target.get(c, 0) + 1
        
        # Initialize window tracking
        window = {}
        have, need = 0, len(target)
        res, res_len = [-1, -1], float("inf")
        l = 0
        
        # Expand window using right pointer
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            # If character count matches target, increment 'have'
            if c in target and window[c] == target[c]:
                have += 1
            
            # Contract window when all target chars are satisfied
            while have == need:
                # Update result if smaller window found
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                # Pop from left
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        
        # Return smallest valid substring
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""