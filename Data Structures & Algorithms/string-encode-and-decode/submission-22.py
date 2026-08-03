class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == "":
            return ""
        if not strs:
            return "[]"
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        elif s == "[]":
            return []
        
        res = []

        i = 0

        while i < len(s):
            length = 0
            number = ""
            for j in range(i, len(s)):
                c = s[j]
                if c != "#":
                    number = number + c
                else:
                    break
            length = int(number)

            res.append(s[i + len(number) + 1 : i + length + len(number) + 1])
            i += length + 1 + len(number)
        return res

        