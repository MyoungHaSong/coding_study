class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split(' ')
        dic = {}
        dic2 = {}
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                dic[pattern[i]] = s[i]
            else:
                if dic[pattern[i]] != s[i]:
                    return False
            if s[i] not in dic2:
                dic2[s[i]] = pattern[i]
            else:
                if dic2[s[i]] != pattern[i]:
                    return False
        else:
            return True
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        for i in range(len(s)):
            p = pattern[i]
            c = s[i]
            p_w = 'pa_%s'%p
            c_w = 'ca_%s'%c
            if p_w not in dic:
                dic[p_w] = i
            if c_w not in dic:
                dic[c_w]=  i
            if dic[p_w] != dic[c_w]:
                return False
        else:
            return True
        
            