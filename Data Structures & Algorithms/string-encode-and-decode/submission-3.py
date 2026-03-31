class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string = string + i + "—"
        return string

    def decode(self, s: str) -> List[str]:
        return s.split("—")[:-1]