class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)


        """
        What we want to do is create a freq map of all the characters in the string
        Then what we can do is start a window, then until the contents of that window are 0 in the freq
        map, we keep expanding thewindow, once they are then we can record the distance in a res list

        so while r < len s
        cur = x: 1, y : 1
        """

        l = r = 0
        cur = {}
        res = []
        while r < len(s):
            c = s[r]
            cur[c] = cur.get(c, freq[c]) - 1
            if cur[c] == 0:
                del cur[c]
            r += 1
            if not cur:
                res.append(r - l)
                l = r
        return res