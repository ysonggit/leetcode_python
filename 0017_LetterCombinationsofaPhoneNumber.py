class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == "":
            return res
        sol = ""
        button_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def dfs(res: List[str], sol: str, digits: str, cur: int, button_map: dict):
            if cur == len(digits):
                res.append(sol)
                return
            letters = button_map[digits[cur]]
            for c in letters:
                sol += c
                dfs(res, sol, digits, cur+1, button_map)
                sol = sol[:-1]
        dfs(res, sol, digits, 0, button_map)
        return res
            
        