class Solution:
    def to_upper(self, str):
        for i in range(len(str)):
            if ('a' <= str[i] <= 'z'):
                str = (str[0:i] + chr(ord(str[i]) -
                                            ord('a') + ord('A')) +
                                            str[i + 1:])
        return str;