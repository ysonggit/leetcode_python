class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        uf = {}
        
        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                uf[py] = px
            
        for a, b in synonyms:
            union(a, b)  
        sydict = defaultdict(set)
        for a, b in synonyms:
            root = find(a)
            sydict[root] |= set([a, b])        
        #for k, v in sydict.items():
        #    print(k, v)
        words = []
        for wd in text.split():
            if wd not in uf:
                words.append([wd])
            else:
                root = find(wd)
                words.append(list(sydict[root]))
        
        res = [" ".join(sentence) for sentence in itertools.product(*words)]
        return sorted(res)
