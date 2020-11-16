class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(timestamp)
        user_ts = defaultdict(list)
        for i in range(n):
            web, t, user = website[i], timestamp[i], username[i]
            user_ts[user].append((t, web))
        # order webs by visiting time
        user_webs = {} # key is user, value is list of websites ordered by timestamp
        for user, ts_webs in user_ts.items():
            user_webs[user] = [ w for _, w in sorted(ts_webs, key=lambda x: x[0])]
            # print(user, user_webs[user])
        webs_seq = defaultdict(set) # key is a combination of 3 websites, vaule is a set of visiting users 
        for u, webs in user_webs.items():
            n = len(webs)
            if n >= 3:
                for i in range(n-2):
                    for j in range(i+1, n-1):
                        for k in range(j+1, n):
                            comb = (webs[i], webs[j], webs[k])
                            webs_seq[comb].add(u)
        #for k, v in webs_seq.items():
        #    print(k, v)
        web_3_sorted = [web for web, user_set in sorted(webs_seq.items(), key=lambda x:(-len(x[1]), x[0]))]  
        return web_3_sorted[0]
