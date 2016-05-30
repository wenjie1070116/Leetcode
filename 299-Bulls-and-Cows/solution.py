import collections
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        hashmap = {}
        i = 0
        A, B = 0, 0
        while i < len(secret):
            if secret[i] == guess[i]:
                A += 1
            else:
                hashmap[secret[i]] = hashmap.get(secret[i], 0) + 1
                if hashmap[secret[i]] <= 0:
                    B += 1
                hashmap[guess[i]] = hashmap.get(guess[i], 0) - 1
                if hashmap[guess[i]] >= 0:
                    B += 1
            i += 1
        return str(A) + 'A' + str(B) + 'B'
        