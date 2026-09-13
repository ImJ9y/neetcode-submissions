class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t, window = {}, {}

        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        
        have, need = 0, len(count_t)
        L = 0
        res, res_len = [-1,-1], float('inf')

        for R in range(len(s)):
            cur_c = s[R]
            window[cur_c] = 1 + window.get(cur_c, 0)

            if cur_c in count_t and count_t[cur_c] == window[cur_c]:
                have += 1

                while need == have:
                    if R - L + 1 < res_len:
                        res_len = R - L + 1
                        res = [L, R]

                    window[s[L]] -= 1

                    if s[L] in count_t and count_t[s[L]] > window[s[L]]:
                        have -= 1

                    L += 1

        L, R = res

        return s[L:R+1] if res_len != float('inf') else ""