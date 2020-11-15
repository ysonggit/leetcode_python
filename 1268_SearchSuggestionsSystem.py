class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        cur = ""
        for c in searchWord:
            cur += c
            i = bisect.bisect_left(products, cur)
            #print(cur, i)
            res.append([w for w in products[i:i+3] if w.startswith(cur)])
        return res
