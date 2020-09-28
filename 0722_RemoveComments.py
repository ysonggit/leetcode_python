class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        orig_str = "\n".join(source)
        new_str = re.sub(r'//.*|/\*(.|\n)*?\*/', "", orig_str)
        return list(filter(None, new_str.split("\n"))) # filter out empty string in arr